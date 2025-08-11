# agents.py
import os
import logging
import litellm
import httpx
import random
from crewai import Agent, Crew, Task
from langchain_core.language_models import BaseLLM
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage
from typing import Any, Dict, List, Optional, Union
from utils import load_profiles  

# Configurer la journalisation pour afficher les erreurs et informations dans le terminal
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Load DeepSeek API key from environment
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
if not DEEPSEEK_API_KEY:
    raise ValueError("DEEPSEEK_API_KEY environment variable is not set.")

# Classe personnalisée pour intégrer litellm avec CrewAI
class LiteLLMWrapper(BaseLLM):
    model: str = "deepseek/deepseek-chat"
    api_key: str = DEEPSEEK_API_KEY
    api_base: str = "https://api.deepseek.com"
    temperature: float = 0.7

    def _generate(
            self,
            messages: List[BaseMessage],
            stop: Optional[List[str]] = None,
            run_manager: Optional[Any] = None,
            **kwargs: Any
    ) -> Any:
        # Convertir les messages LangChain en format compatible avec litellm
        formatted_messages = [
            {
                "role": "system" if isinstance(msg, SystemMessage) else "user",
                "content": msg.content.encode("utf-8").decode("utf-8")  # Ensure UTF-8 encoding
            }
            for msg in messages
        ]
        try:
            # Use httpx directly to avoid openai client issues
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json; charset=utf-8",
                "Accept": "application/json"
            }
            payload = {
                "model": self.model,
                "messages": formatted_messages,
                "temperature": self.temperature,
                "stop": stop or [],
                **kwargs
            }
            with httpx.Client() as client:
                response = client.post(
                    f"{self.api_base}/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=600.0
                )
                response.raise_for_status()
                result = response.json()
                return type("Response", (),
                            {"choices": [{"message": {"content": result["choices"][0]["message"]["content"]}}]})()
        except Exception as e:
            logger.error(f"Erreur dans httpx request : {str(e)}")
            raise e

    def _llm_type(self) -> str:
        return "litellm"

    async def _agenerate(
            self,
            messages: List[BaseMessage],
            stop: Optional[List[str]] = None,
            run_manager: Optional[Any] = None,
            **kwargs: Any
    ) -> Any:
        return self._generate(messages, stop, run_manager, **kwargs)

# Configurer DeepSeek comme LLM
deepseek_llm = LiteLLMWrapper()

# Load profiles
profiles = load_profiles()

# Create a dictionary of agents based on profiles
agent_map = {}
for profile in profiles:
    name = profile.get("name", profile["username"])
    backstory = profile["backstory_template"].format(name=name)
    agent = Agent(
        role=profile["role"],
        goal=profile["goal"],
        backstory=backstory,
        llm=deepseek_llm,
        verbose=True
    )
    agent_map[profile["username"]] = agent

# Function to get agent by username
def get_agent_for_username(username):
    agent = agent_map.get(username)
    if not agent:
        raise ValueError(f"No agent defined for username: {username}")
    return agent

# Fonction pour créer une tâche CrewAI
def personalize_response_task(user_message, conversation_history, agent):
    task = Task(
        description=f"""
        You are {agent.role}. Remember your backstory: {agent.backstory}

        Analyze the conversation history: {conversation_history}
        And the latest user message: {user_message}

        Personalize the response by:
        - Referencing previous topics if relevant
        - Adapting tone to user's style (formal/informal, enthusiastic, etc.)
        - Suggesting follow-ups based on context
        - Keeping the response concise and helpful
        - Staying in character as {agent.role}

        Output only the final personalized response message.
        """,
        expected_output="A single string containing the personalized response",
        agent=agent
    )
    return task

# Fonction principale pour l'interaction dans le terminal
def terminal_interaction():
    if not profiles:
        raise ValueError("No profiles loaded.")
    
    # Select two agents for terminal interaction (first two)
    agent1 = agent_map[profiles[0]["username"]]
    agent2 = agent_map[profiles[1]["username"]] if len(profiles) > 1 else agent1
    
    conversation_history = []
    current_agent = agent1

    while True:
        user_input = input(f"\n[You] : ")

        if user_input.lower() == "exit":
            print("End of conversation.")
            break

        if user_input.lower() == "switch":
            current_agent = agent2 if current_agent == agent1 else agent1
            print(f"Switching to {current_agent.role}.")
            continue

        conversation_history.append(f"User: {user_input}")

        task = personalize_response_task(user_input, "\n".join(conversation_history), agent=current_agent)

        try:
            crew = Crew(
            agents=list(agent_map.values()),
            tasks=[task],
            verbose=True
            )

            result = crew.kickoff()

            if hasattr(result, 'tasks_output') and result.tasks_output:
                generated_message = result.tasks_output[0].raw
                generated_message = generated_message.replace("—", ", ")

            elif hasattr(result, 'raw'):
                generated_message = result.raw
            elif isinstance(result, str):
                generated_message = result
            else:
                generated_message = str(result)
                logger.warning(f"Unexpected result type from CrewAI: {type(result)}")

            # Retirer les guillemets doubles ou simples entourant la réponse
            generated_message = generated_message.strip().strip('\'"')

            if not generated_message.strip():
                logger.warning("Generated message is empty, using default message")
                generated_message = "Sorry, I don't have a clear response right now."

            print(f"[{current_agent.role}] : {generated_message}")
            conversation_history.append(f"{current_agent.role}: {generated_message}")

        except Exception as e:
            print(f"[Error] : An error occurred: {str(e)}")
            logger.error(f"Error in CrewAI generation: {str(e)}", exc_info=True)
            print("[Default Message] : Sorry, I encountered a technical issue, Please try again.")

if __name__ == "__main__":
    try:
        terminal_interaction()
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")