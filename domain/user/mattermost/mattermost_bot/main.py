# main.py
import time
import requests
from config import MATTERMOST_URL, ADMIN_TOKEN, ADMIN_CREDENTIALS, logging
from utils import load_profiles
from api import create_account, authenticate_admin, create_team, add_user_to_team, create_dm_channel
from bot import start_auto_reply_bot
from levels import main as levelbot_main
logger = logging.getLogger(__name__)

def setup_mattermost():
    global ADMIN_TOKEN
    logger.info("Waiting for Mattermost server to start...")
    for _ in range(60):
        try:
            response = requests.get(f"{MATTERMOST_URL}/users", timeout=10)
            logger.info("Mattermost server is accessible")
            break
        except requests.exceptions.ConnectionError:
            logger.warning("Server not ready, waiting 5 seconds...")
            time.sleep(5)
    else:
        logger.error("Mattermost server is not accessible")
        raise Exception("Mattermost server is not accessible")

    logger.info("Creating admin account...")
    try:
        admin_user_id = create_account(ADMIN_CREDENTIALS)
        if not admin_user_id:
            logger.error("Failed to create or retrieve admin account")
            raise Exception("Failed to create or retrieve admin account")
    except Exception as e:
        logger.error(f"Failed to create admin account: {str(e)}")
        raise

    try:
        logger.info(f"Attempting admin login with {ADMIN_CREDENTIALS['login_id']}")
        admin_user_id = authenticate_admin()
        logger.info(f"Logged in with admin account: {admin_user_id}")
    except Exception as e:
        logger.error(f"Failed to login with admin account: {str(e)}")
        raise Exception(f"Cannot proceed without valid admin credentials: {str(e)}")

    team_id = create_team()  # Créer ou récupérer l'équipe
    add_user_to_team(team_id, admin_user_id)  # Ajouter l'admin à l'équipe

    profiles = load_profiles()
    for profile in profiles:
        try:
            user_id = create_account(profile)
            if user_id:
                add_user_to_team(team_id, user_id)  # Ajouter l'utilisateur à l'équipe
                create_dm_channel(admin_user_id, user_id)
                start_auto_reply_bot(profile["username"], profile["password"])
        except Exception as e:
            logger.error(f"Failed to set up user {profile['username']}: {str(e)}")
            continue  # Continuer avec le profil suivant en cas d'erreur

    # Keep the main process running to prevent daemon threads from stopping
    try:
        logger.info("Starting Levelbot...")
        levelbot_main()
    except Exception as e:
        logger.exception("Failed to start Levelbot")
    while True:
        time.sleep(60)  # Sleep indefinitely to keep the process alive

if __name__ == "__main__":
    try:
        setup_mattermost()
    except Exception as e:
        logging.getLogger('main').error(f"Script failed: {str(e)}")
        raise