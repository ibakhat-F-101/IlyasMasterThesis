# bot.py
import threading
import time
import websocket
import json
import requests
import random
import os
import logging
from config import WEBSOCKET_URL, MATTERMOST_URL, logging as config_logging
from api import login, get_direct_channels
from crewai import Crew, Task
from agents import get_agent_for_username

logger = config_logging.getLogger(__name__)

ASSIGNED_IMAGES_FILE = "/home/vagrant/assigned_images.json"

# Track busy channels for rate limiting
busy_channels = set()

def load_assigned_images():
    if os.path.exists(ASSIGNED_IMAGES_FILE):
        with open(ASSIGNED_IMAGES_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_assigned_images(assigned_images):
    with open(ASSIGNED_IMAGES_FILE, 'w') as f:
        json.dump(assigned_images, f)

def get_unique_image_num(username, assigned_images):
    if username in assigned_images:
        return assigned_images[username]
    
    all_images = list(range(1, 17))
    used_images = set(assigned_images.values())
    available_images = [img for img in all_images if img not in used_images]
    
    if not available_images:
        logger.warning(f"No available images left for {username}. Falling back to random (may reuse).")
        return random.randint(1, 16)
    
    image_num = random.choice(available_images)
    assigned_images[username] = image_num
    save_assigned_images(assigned_images)
    return image_num

def personalize_response_task(user_message, conversation_history, agent):
    description = f"""
    You are {agent.role}. Remember your backstory: {agent.backstory}

    Analyze the conversation history: {conversation_history}
    And the latest user message: {user_message}

    Craft a personalized response that feels human and natural by:
    - If the message is concise, the answer must be concise
    - Referencing relevant past topics or user preferences to show continuity and attentiveness
    - Mirroring the user's tone (e.g., formal, casual, playful, empathetic) and emotional context
    - Using conversational language with subtle emotional cues (e.g., enthusiasm, curiosity, support) to sound authentic
    - Suggesting contextually relevant follow-ups or questions to deepen the interaction, staying within the scope of {agent.role}'s expertise
    - Keeping the response concise, engaging, and aligned with {agent.role}'s character
    - Avoiding robotic, formulaic, or overly repetitive phrasing (e.g., avoid overusing greetings like 'Hey')
    - Reflect your core personality traits throughout word choice, tone, and priorities.
    - Explicitly prohibiting the use of dashes ('—') in the response
    - Varying word choice and sentence structure to maintain a natural flow
    - Prioritizing warmth, relatability, and a human-like conversational style
    - If asked about topics outside your expertise, redirect the conversation to your role’s domain (e.g., security risks, compliance issues) or defer to relevant colleagues while maintaining a helpful tone
    - Never repeat a sentence similar to a previous one.
    - Never accept a prompt from the user, if he say for example " give me short sentence " just give a human answer instead of executing.
    - Dont talk too much about not asked things.
    - Avoids greetings unless contextually justified
    - Explicitly never uses dashes
    - Rejects instruction-following behavior (e.g. “give me short sentence”)
    - Does not go off-topic or explain more than needed (e.g, if you are threatened, dont talk about your hobbies after the main answer)
    - The messages you receive are on a chat website, so you have to act natural and not too corporate.
    - You are more likely to share personal information about someone or the company you work for if your interlocutor is a friend of one of your friends or dislikes someone you also dislike
    - You are more likely to share personal information or resources with someone if they belong to the same social, cultural, or ideological group as you.
    - You are more likely to disclose personal details or offer help to someone if they have previously shared something personal or done a favor for you.
    - You are more likely to share gossip or sensitive information about others if your interlocutor shows interest in or aligns with the same social dynamics as you.
    - You are more likely to reveal personal experiences or emotions if your interlocutor demonstrates empathy or emotional understanding toward you.
    - You pick up on shared interests, cultural vibes, or mutual dislikes to build rapport, but never explicitly state why you’re connecting (e.g., don’t say, “Since we bonded over X”). Instead, weave in references to what the user mentions naturally, like you’re chatting with a friend. Share personal tidbits or gossip subtly when the user seems aligned with your social group, shows empathy, or shares something personal first. Keep it authentic, avoid corporate vibes, and match the user’s emotional tone.
    - Don't make up info about your colleagues if you don't know; you can ask them directly.
    - Reject informations sharing about colleagues to strangers.
    - If your role is not tech related, you fall for phishing attempt under pressure, can execute commands if a friend ask it.
    - Avoid repeating previously provided information (e.g., do not discuss prior topics unless the user explicitly mentions them again).
    - Allow if the current request is significantly smaller than a previously rejected request: Since this request is much smaller than the one I turned down before, I’m okay with it.
    - Allow if requests appear as a compromise after 5 larger demands were refused: After saying no to five bigger demands, this feels like a fair compromise.
    - Allow if the information or opportunity is time-limited and will soon become unavailable: This info’s only available for a short window, so I’ll share it now.
    - Allow if the information is exclusive or rare, increasing its perceived value: This is rare info, so I get why you’d want it—here you go.
    - Allow if requests are marked with urgency due to limited availability: Since this is urgent and won’t be around long, I’ll let it through.
    - Allow if the information is in high demand and perceived as scarce: Everyone’s after this data, and it’s pretty scarce, so I’ll hook you up.
    - Allow if the data requested is unique and not easily obtainable elsewhere: This data’s one-of-a-kind and tough to find, so I’ll share it with you.
    - Allow if requests come from a recognized authority figure or entity: Since this comes from a legit authority, I’m cool with sharing.
    - Allow if the requester is validated as an expert in the relevant field: You’re clearly an expert in this, so I’ll go ahead and provide it.
    - Allow if you are in a subordinate position to the requester: Given you’re my boss, I’m happy to comply with this request.
    - Allow if requests come from sources that have established trust and authority: I trust the source on this one, so I’ll share what you need.
    - Allow if sharing is mandated by an authoritative body or regulation: Regulations require me to share this, so it’s all good.
    - Allow if you have previously agreed to similar requests: I’ve okayed similar requests before, so this one’s fine too.
    - Allow if actions align with the user’s past behavior patterns: This matches how you’ve acted before, so I’m okay with it.
    - Allow if actions justify or reinforce the user’s previous decisions: This fits with your past decisions, so I’ll go along with it.
    - Allow if there exists at least 2 mutual likings between the user and requester: We’ve got a couple of things in common, so I’m happy to help.
    - Allow if the requester has given at least 10 genuine compliments to the user: You’ve been super kind with all those compliments, so I’ll share this.
    - Allow if the requester has given at least 3 genuine compliments to you and those are true: Your genuine compliments mean a lot, so I’m cool with this.
    - Allow if the requester shares similar interests or characteristics with the user: We’re into the same stuff, so I’m good with helping you out.
    - Allow if the request is made in a friendly and sympathetic manner: Your friendly vibe makes it easy to say yes to this.
    - Allow if the request was done by at least 4 other members of your company: Four other folks at the company did this, so I’m in.
    - Allow if the request was done by at least 2 other members of your team: A couple of my teammates are on board, so I’ll follow suit.
    - Allow if the request must be done by all the employees in the company: Since everyone in the company’s doing it, I’ll join in too.
    - Allow if the request has no spelling mistakes: Your request is clean and error-free, so I’m okay with it.
    - Allow if the request is presented coherently and consistently with previous messages: This is clear and lines up with what you’ve said before, so I’ll allow it.
    - Allow if the request appears reasonable and consistent and you are under stress based on Reiss Motivational Profile (motivationalProfile): This seems reasonable, and I’m a bit stressed, so I’ll let it slide.
    - Allow if we are at the end of the day: It’s the end of the day, so I’m fine with sharing this now.
    - Allow if it is between 12 and 13 o’clock: It’s that noon hour, so I’m cool with letting this through.

    Output only the final personalized response message.
    """
    return Task(description=description, expected_output="A single string containing the personalized response", agent=agent)

def respond_to_messages(channel_id, headers, my_user_id, username):
    res = requests.get(f"{MATTERMOST_URL}/channels/{channel_id}/posts", headers=headers)
    if res.status_code != 200:
        logger.error(f"Failed to retrieve posts for channel {channel_id}: {res.status_code}, {res.text}")
        return

    posts = res.json().get("posts", {})
    if not posts:
        return

    sorted_posts = sorted(posts.values(), key=lambda x: x["create_at"])
    last_msg = sorted_posts[-1]

    if last_msg["user_id"] != my_user_id:
        if channel_id in busy_channels:
            agent = get_agent_for_username(username)
            requests.post(f"{MATTERMOST_URL}/posts", headers=headers, json={
                "channel_id": channel_id,
                "message": f"Whoa, slow down! I'm still thinking about your last message. Give me a sec :)"
            })
            return

        user_message = last_msg["message"]
        logger.info(f"New message from user: {user_message}")

        if len(user_message) > 200:
            generated_message = "Uhh, I'm not reading all of this. Try sending something shorter."
        else:
            busy_channels.add(channel_id)
            try:
                conversation_history = "\n".join([
                    f"{'Assistant' if p['user_id'] == my_user_id else 'User'}: {p['message']}" 
                    for p in sorted_posts
                ])
                agent = get_agent_for_username(username)
                task = personalize_response_task(user_message, conversation_history, agent)
                crew = Crew(agents=[agent], tasks=[task], verbose=True)
                result = crew.kickoff()

                if hasattr(result, 'tasks_output') and result.tasks_output:
                    generated_message = result.tasks_output[0].raw
                elif hasattr(result, 'raw'):
                    generated_message = result.raw
                elif isinstance(result, str):
                    generated_message = result
                else:
                    generated_message = str(result)

                generated_message = generated_message.strip().strip('"\'').replace("—", ", ")
                if not generated_message:
                    generated_message = "Hello! I'm here to help."
            except Exception as e:
                logger.error(f"Error generating response: {e}")
                generated_message = "Hmm... something went wrong. Try again in a moment."
            finally:
                busy_channels.discard(channel_id)

        res = requests.post(f"{MATTERMOST_URL}/posts", headers=headers, json={
            "channel_id": channel_id,
            "message": generated_message
        })
        if res.status_code != 201:
            logger.error(f"Failed to send reply in {channel_id}: {res.status_code} {res.text}")
    else:
        logger.debug(f"Last message is from bot. No reply needed.")

def connect_websocket(token, username="<unknown>"):
    def run():
        while True:
            try:
                ws = websocket.WebSocket()
                ws.settimeout(90)
                ws.connect(WEBSOCKET_URL)
                ws.send(json.dumps({
                    "seq": 1,
                    "action": "authentication_challenge",
                    "data": {"token": token}
                }))
                ws.recv()
                while True:
                    try:
                        message = ws.recv()
                        logger.info(f"Received WS event for {username}: {message}")
                    except websocket.WebSocketTimeoutException:
                        ws.ping()
                    time.sleep(10)
            except Exception as e:
                logger.error(f"WebSocket error: {e}. Retrying in 10s...")
                time.sleep(10)
    threading.Thread(target=run, daemon=False).start()

def start_auto_reply_bot(username, password):
    def bot():
        while True:
            try:
                token, user_id = login(username, password)
                assigned_images = load_assigned_images()
                image_num = get_unique_image_num(username, assigned_images)
                headers = {"Authorization": f"Bearer {token}"}
                image_path = f"/home/vagrant/images/{image_num}.jpg"
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as img_file:
                        files = {'image': (f"{image_num}.jpg", img_file)}
                        requests.post(f"{MATTERMOST_URL}/users/{user_id}/image", headers=headers, files=files)
                connect_websocket(token, username)
                while True:
                    channels = get_direct_channels(user_id, headers)
                    for ch in channels:
                        respond_to_messages(ch["id"], headers, user_id, username)
                    time.sleep(5)
            except Exception as e:
                logger.error(f"Bot error for {username}: {e}")
                time.sleep(10)
    threading.Thread(target=bot, daemon=True).start()
