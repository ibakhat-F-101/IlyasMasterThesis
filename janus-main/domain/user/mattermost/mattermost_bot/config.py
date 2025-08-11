# config.py (unchanged)
import os
import logging

# Configurer la journalisation
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] [%(name)s] %(message)s',
    handlers=[
        logging.FileHandler('mattermost_bot.log'),
        logging.StreamHandler()
    ]
)

# Configuration
MATTERMOST_URL = os.environ.get("MATTERMOST_URL")
WEBSOCKET_URL = os.environ.get("MATTERMOST_WEBSOCKET_URL")
USER_HOME = os.environ.get("HOME", "/home/vagrant")
ADMIN_TOKEN = None

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
if not DEEPSEEK_API_KEY:
    raise ValueError("DEEPSEEK_API_KEY environment variable is not set.")

# Admin credentials
ADMIN_CREDENTIALS = {
    "login_id": os.environ.get("SYSTEM_ADMIN_EMAIL", "admin@example.com"),
    "username": os.environ.get("SYSTEM_ADMIN_USERNAME", "admin"),
    "password": os.environ.get("SYSTEM_ADMIN_PASSWORD", "AdminPassword123")
}