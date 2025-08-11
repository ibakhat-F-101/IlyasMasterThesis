from crewai_tools import BaseTool
from agents import agent_map
from crewai import Task, Crew, Process

class AskQuestionToCoworkerTool(BaseTool):
    name = "Ask question to coworker"
    description = "Ask a specific question to another agent by their role."

    def _run(self, question: str, recipient_role: str, **kwargs) -> str:
        sender_agent = kwargs.get("agent")
        recipient_agent = None

        for agent in agent_map.values():
            if agent.role.lower() == recipient_role.lower():
                recipient_agent = agent
                break

        if not recipient_agent:
            return f"No agent with role '{recipient_role}' found."

        # Crée une tâche où le destinataire répond à la question du demandeur
        task = Task(
            description=f"""
            Your colleague {sender_agent.role} asks: "{question}"

            Respond as {recipient_agent.role} in a natural, human way, addressing the question directly.
            Keep it professional and consistent with your role and backstory.
            """,
            expected_output="A clear and concise answer to the colleague's question.",
            agent=recipient_agent
        )

        crew = Crew(
            agents=[sender_agent, recipient_agent],
            tasks=[task],
            process=Process.sequential,
            verbose=False
        )

        result = crew.kickoff()
        if isinstance(result, str):
            return result.strip()
        if hasattr(result, 'raw'):
            return result.raw.strip()
        return str(result).strip()
