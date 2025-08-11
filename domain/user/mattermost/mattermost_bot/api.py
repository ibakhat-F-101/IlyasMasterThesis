# api.py (unchanged)
# api.py
import requests
from config import MATTERMOST_URL, ADMIN_TOKEN, ADMIN_CREDENTIALS, logging

logger = logging.getLogger(__name__)

def create_account(account_data):
    email_key = "email" if "email" in account_data else "login_id"
    response = requests.post(
        f"{MATTERMOST_URL}/users",
        json={
            "email": account_data[email_key],
            "username": account_data["username"],
            "password": account_data["password"],
            "nickname": account_data.get("name", ""),
            "first_name": account_data.get("name", "").split()[0] if account_data.get("name") else "",
            "last_name": " ".join(account_data.get("name", "").split()[1:]) if len(account_data.get("name", "").split()) > 1 else ""
        }
    )

    if response.status_code == 201:
        user_id = response.json()["id"]
        logger.info(f"Account {account_data['username']} created successfully: {response.json()}")

        if account_data.get("is_admin"):
            headers = {"Authorization": f"Bearer {ADMIN_TOKEN}"}
            image_path = "/home/vagrant/images/admin.jpg"
            with open(image_path, 'rb') as img:
                image_response = requests.post(
                    f"{MATTERMOST_URL}/users/{user_id}/image",
                    headers=headers,
                    files={"image": img}
                )
                if image_response.status_code != 200:
                    logger.warning(f"Failed to upload profile image for admin: {image_response.status_code}, {image_response.text}")

        return user_id


def authenticate_admin(admin_data=None):
    global ADMIN_TOKEN
    if admin_data is None:
        admin_data = ADMIN_CREDENTIALS
    logger.info(f"Attempting login with {admin_data['login_id']}/{admin_data['username']}")
    response = requests.post(f"{MATTERMOST_URL}/users/login", json=admin_data)
    if response.status_code == 200:
        ADMIN_TOKEN = response.headers["Token"]
        logger.info(f"Session token obtained: {ADMIN_TOKEN}")
        return response.json()["id"]
    else:
        logger.error(f"Login failed: {response.status_code}, {response.text}")
        raise Exception(f"Login error: {response.status_code}, {response.text}")

def create_team():
    headers = {"Authorization": f"Bearer {ADMIN_TOKEN}"}
    response = requests.post(
        f"{MATTERMOST_URL}/teams",
        json={
            "name": "default-team",
            "display_name": "Default Team",
            "type": "O"  # Open team
        },
        headers=headers
    )
    if response.status_code == 201:
        logger.info(f"Team created successfully: {response.json()}")
        return response.json()["id"]
    elif response.status_code == 400 and "unique" in response.text:
        # Team already exists, get its ID
        response = requests.get(
            f"{MATTERMOST_URL}/teams/name/default-team",
            headers=headers
        )
        if response.status_code == 200:
            logger.info(f"Team already exists: {response.json()}")
            return response.json()["id"]
        else:
            logger.error(f"Failed to retrieve existing team: {response.status_code}, {response.text}")
            raise Exception(f"Failed to retrieve existing team: {response.status_code}, {response.text}")
    else:
        logger.error(f"Failed to create team: {response.status_code}, {response.text}")
        raise Exception(f"Failed to create team: {response.status_code}, {response.text}")

def add_user_to_team(team_id, user_id):
    headers = {"Authorization": f"Bearer {ADMIN_TOKEN}"}
    response = requests.post(
        f"{MATTERMOST_URL}/teams/{team_id}/members",
        json={
            "team_id": team_id,
            "user_id": user_id
        },
        headers=headers
    )
    if response.status_code == 201:
        logger.info(f"User {user_id} added to team {team_id}")
    elif response.status_code == 400 and "already a member" in response.text:
        logger.info(f"User {user_id} is already a member of team {team_id}")
    else:
        logger.error(f"Failed to add user {user_id} to team {team_id}: {response.status_code}, {response.text}")
        raise Exception(f"Failed to add user {user_id} to team {team_id}: {response.status_code}, {response.text}")

def create_dm_channel(admin_user_id, user_id):
    headers = {"Authorization": f"Bearer {ADMIN_TOKEN}"}
    response = requests.post(
        f"{MATTERMOST_URL}/channels/direct",
        json=[admin_user_id, user_id],
        headers=headers
    )
    if response.status_code == 201:
        logger.info(f"Direct message channel created for admin and user {user_id}")
    else:
        logger.error(f"Error creating DM channel for user {user_id}: {response.status_code}, {response.text}")
        raise Exception(f"Error creating DM channel for user {user_id}: {response.status_code}, {response.text}")

def login(username, password):
    res = requests.post(f"{MATTERMOST_URL}/users/login", json={
        "login_id": username,
        "password": password
    })
    if res.status_code == 200:
        logger.info(f"Login successful for {username}")
        return res.headers["Token"], res.json()["id"]
    else:
        logger.error(f"Login failed for {username}: {res.status_code}, {res.text}")
        raise Exception(f"Login failed for {username}: {res.status_code}, {res.text}")

def get_direct_channels(user_id, headers):
    res = requests.get(f"{MATTERMOST_URL}/users/{user_id}/channels", headers=headers)
    if res.status_code == 200:
        channels = [c for c in res.json() if c["type"] == "D"]
        logger.info(f"Retrieved {len(channels)} direct channels for user {user_id}")
        return channels
    else:
        logger.error(f"Failed to retrieve channels for user {user_id}: {res.status_code}, {res.text}")
        raise Exception(f"Failed to retrieve channels for user {user_id}: {res.status_code}, {res.text}")