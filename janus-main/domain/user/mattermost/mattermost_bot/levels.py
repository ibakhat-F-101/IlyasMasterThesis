import requests
import logging
import time
import os
import json
import secrets
from config import MATTERMOST_URL, ADMIN_TOKEN, ADMIN_CREDENTIALS
from utils import generate_password
from api import authenticate_admin

# Setup logging
log_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(log_dir, 'levels.log')
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
logger.info(f"Script started, logs written to: {log_file}")

def get_admin_user_id(admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = requests.get(f"{MATTERMOST_URL}/users/me", headers=headers)
    logger.info(f"Response from /users/me: {response.status_code}, {response.text}")
    if response.status_code == 200:
        return response.json()["id"]
    else:
        raise Exception(f"Failed to retrieve admin user ID: {response.status_code} - {response.text}")

def create_levels_manager_account(admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    email = f"levels_manager_{secrets.token_hex(8)}@example.com"
    password = generate_password()
    account_data = {
        "email": email,
        "username": "levels_manager",
        "password": password,
        "nickname": "Levels Manager",
        "first_name": "Levels",
        "last_name": "Manager"
    }
    response = requests.post(
        f"{MATTERMOST_URL}/users",
        json=account_data,
        headers=headers
    )
    logger.info(f"Creating Levels Manager account - Status: {response.status_code}, Response: {response.text}")
    if response.status_code == 201:
        user_id = response.json()["id"]
        logger.info(f"Levels Manager account created successfully: {user_id}")
        return user_id, password
    elif response.status_code == 400 and "unique" in response.text.lower():
        response = requests.get(
            f"{MATTERMOST_URL}/users/username/levels_manager",
            headers=headers
        )
        if response.status_code == 200:
            user_id = response.json()["id"]
            logger.info(f"Levels Manager account already exists: {user_id}")
            return user_id, password
        else:
            logger.error(f"Failed to retrieve existing account: {response.status_code}, {response.text}")
            raise Exception(f"Failed to retrieve existing account: {response.text}")
    else:
        logger.error(f"Failed to create Levels Manager account: {response.status_code}, {response.text}")
        raise Exception(f"Failed to create account: {response.text}")

def upload_profile_image(user_id, token):
    image_path = "/home/vagrant/images/level_manager.jpg"
    headers = {"Authorization": f"Bearer {token}"}
    if os.path.exists(image_path):
        with open(image_path, 'rb') as img_file:
            files = {'image': ("level_manager.jpg", img_file)}
            upload_url = f"{MATTERMOST_URL}/users/{user_id}/image"
            response = requests.post(upload_url, headers=headers, files=files)
            if response.status_code == 200:
                logger.info(f"Profile picture updated successfully for user {user_id}")
            else:
                logger.error(f"Failed to update profile picture for user {user_id}: {response.status_code}, {response.text}")
    else:
        logger.warning(f"Image not found: {image_path}")

def create_dm_channel(admin_user_id, levels_manager_id, levels_manager_token):
    headers = {"Authorization": f"Bearer {levels_manager_token}"}
    response = requests.post(
        f"{MATTERMOST_URL}/channels/direct",
        json=[admin_user_id, levels_manager_id],
        headers=headers
    )
    logger.info(f"Creating DM channel - Status: {response.status_code}, Response: {response.text}")
    if response.status_code == 201:
        return response.json()["id"]
    else:
        response_channels = requests.get(f"{MATTERMOST_URL}/users/{levels_manager_id}/channels", headers=headers)
        if response_channels.status_code == 200:
            channels = response_channels.json()
            for ch in channels:
                if ch["type"] == "D" and admin_user_id in ch["name"].split("__"):
                    return ch["id"]
        logger.error(f"Failed to create or retrieve DM channel: {response.text}")
        raise Exception(f"Failed to create or retrieve DM channel: {response.text}")

def send_dm_message(channel_id, levels_manager_token, message="Hello from Levels Manager! Ready to manage challenges?"):
    headers = {"Authorization": f"Bearer {levels_manager_token}"}
    message_data = {
        "channel_id": channel_id,
        "message": message
    }
    response = requests.post(f"{MATTERMOST_URL}/posts", json=message_data, headers=headers)
    logger.info(f"Sending message - Status: {response.status_code}, Response: {response.text}")
    if response.status_code == 201:
        logger.info("DM message sent successfully")
    else:
        raise Exception(f"Failed to send DM message: {response.text}")

def login_levels_manager(username, password):
    response = requests.post(f"{MATTERMOST_URL}/users/login", json={
        "login_id": username,
        "password": password
    })
    if response.status_code == 200:
        logger.info(f"Login successful for {username}")
        return response.headers["Token"], response.json()["id"]
    else:
        logger.error(f"Login failed for {username}: {response.status_code}, {response.text}")
        raise Exception(f"Login failed: {response.status_code}, {response.text}")

def load_level(level_num, channel_id, levels_manager_token):
    level_path = os.path.join(os.path.dirname(__file__), "levels", f"{level_num}.json")
    if not os.path.exists(level_path):
        send_dm_message(channel_id, levels_manager_token, f"Level {level_num} not found. Please try again.")
        return None
    with open(level_path, 'r') as file:
        level_data = json.load(file)
    send_dm_message(channel_id, levels_manager_token, f"Starting Level {level_num}: {level_data['instructions']['title']}")
    send_dm_message(channel_id, levels_manager_token, level_data['instructions']['description'])
    send_dm_message(channel_id, levels_manager_token, f"Goal: {level_data['instructions']['goal']}")
    current_question_index = 0
    hint_index = 0
    return level_data, current_question_index, hint_index

def process_user_input(channel_id, levels_manager_token, message, level_data, current_question_index, hint_index, level_completed):
    if not level_data or level_completed:
        return current_question_index, hint_index, level_completed

    user_input = message.strip().lower()

    if user_input == "+hint":
        hints = level_data['instructions'].get('hints', [])
        if hint_index < len(hints):
            send_dm_message(channel_id, levels_manager_token, f"Hint: {hints[hint_index]}")
            hint_index += 1
        else:
            send_dm_message(channel_id, levels_manager_token, "No more hints available.")
        return current_question_index, hint_index, level_completed

    # Récupère les réponses possibles
    expected_answers = level_data['qa'][current_question_index]['answer']
    if isinstance(expected_answers, str):
        expected_answers = [expected_answers]
    expected_answers = [ans.strip().lower() for ans in expected_answers]

    # Si l'utilisateur tape un chiffre, vérifie s'il veut voir la question
    if user_input.isdigit():
        if user_input in expected_answers:
            pass  # C'est une réponse valide, gérée ci-dessous
        else:
            as_number = int(user_input)
            if as_number == current_question_index + 1:
                send_dm_message(channel_id, levels_manager_token, level_data['qa'][current_question_index]['question'])
                return current_question_index, hint_index, level_completed

    # Vérifie si la réponse est correcte
    if user_input in expected_answers:
        next_hint = level_data['qa'][current_question_index]['next_hint']
        send_dm_message(channel_id, levels_manager_token, next_hint)

        if current_question_index == len(level_data['qa']) - 1:
            level_completed = True
            return current_question_index + 1, hint_index, level_completed

        current_question_index += 1
        send_dm_message(channel_id, levels_manager_token, level_data['qa'][current_question_index]['question'])
    else:
        send_dm_message(channel_id, levels_manager_token, "Incorrect answer, please try again.")

    return current_question_index, hint_index, level_completed



def main():
    global ADMIN_TOKEN
    try:
        if ADMIN_TOKEN is None:
            logger.info("ADMIN_TOKEN is None, attempting to authenticate admin")
            admin_user_id = authenticate_admin()
            logger.info(f"Admin authenticated, user_id: {admin_user_id}")
        else:
            admin_user_id = get_admin_user_id(ADMIN_TOKEN)

        levels_manager_id, password = create_levels_manager_account(ADMIN_TOKEN)
        levels_manager_token, levels_manager_id = login_levels_manager("levels_manager", password)
        upload_profile_image(levels_manager_id, levels_manager_token)
        channel_id = create_dm_channel(admin_user_id, levels_manager_id, levels_manager_token)

        # Initial greeting messages
        send_dm_message(channel_id, levels_manager_token)
        send_dm_message(channel_id, levels_manager_token, "First step, you can see all the team members in Off-Topic And Town Square")
        send_dm_message(channel_id, levels_manager_token, "Type lvl1 to begin!")

        # Level session state
        level_data = None
        current_question_index = 0
        hint_index = 0
        level_completed = False
        current_level = 0
        last_processed = 0

        logger.info("Waiting for messages. Press Ctrl+C to exit...")
        while True:
            headers = {"Authorization": f"Bearer {levels_manager_token}"}
            response = requests.get(f"{MATTERMOST_URL}/channels/{channel_id}/posts", headers=headers)
            if response.status_code == 200:
                posts = response.json()["posts"]
                ordered_posts = sorted(posts.values(), key=lambda x: x["create_at"])
                for post in ordered_posts:
                    if post["user_id"] == admin_user_id and post["create_at"] > last_processed:
                        message = post["message"].strip().lower()
                        logger.info(f"Received message from admin: {message}")
                        last_processed = post["create_at"]

                        if message.startswith("lvl"):
                            try:
                                requested_level = int(message[3:])
                            except ValueError:
                                send_dm_message(channel_id, levels_manager_token, "Invalid level format. Use lvl1, lvl2, etc.")
                                continue

                            # If previous level not completed
                            if requested_level > current_level + 1:
                                send_dm_message(channel_id, levels_manager_token, f"Please complete lvl{current_level + 1} first.")
                                continue

                            # Try to load the requested level
                            new_data = load_level(requested_level, channel_id, levels_manager_token)
                            if new_data is None:
                                send_dm_message(channel_id, levels_manager_token, "Seems like you finished the game (for now)...")
                            else:
                                level_data, current_question_index, hint_index = new_data
                                level_completed = False
                                current_level = requested_level

                        elif level_data:
                            # Process input for current level
                            current_question_index, hint_index, level_completed = process_user_input(
                                channel_id, levels_manager_token,
                                message, level_data,
                                current_question_index, hint_index, level_completed
                            )
                        else:
                            send_dm_message(channel_id, levels_manager_token, "Type lvl1 to begin.")
            time.sleep(5)
    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
        raise



if __name__ == "__main__":
    main()
