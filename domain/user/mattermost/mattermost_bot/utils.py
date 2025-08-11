# utils.py
import secrets
import string
import json
import random
import os
from config import USER_HOME, logging
from behaviors import roles_behaviors, contradictory_pairs, is_valid_combination, calculate_joint_prob

logger = logging.getLogger(__name__)

ROLES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'roles.json')
try:
    with open(ROLES_FILE, 'r') as f:
        ROLES_DICT = json.load(f)['roles']
    logger.info(f"ROLES_DICT loaded successfully from {ROLES_FILE}")
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.warning(f"Erreur lors du chargement de {ROLES_FILE}: {str(e)}. Utilisation d'un ROLES_DICT vide.")
    ROLES_DICT = {}

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

def assign_personality_traits(role, num_traits=5):
    if role not in roles_behaviors:
        logger.warning(f"Role {role} not found in roles_behaviors, assigning default traits")
        return ["Kindness", "Resilience", "Honesty"]
    
    behaviors = list(roles_behaviors[role].keys())
    max_attempts = 100
    best_combination = []
    best_prob = 0.0

    for _ in range(max_attempts):
        combination = random.sample(behaviors, min(num_traits, len(behaviors)))
        if is_valid_combination(combination):
            prob = calculate_joint_prob(role, combination)
            if prob > best_prob:
                best_prob = prob
                best_combination = combination

    if not best_combination:
        logger.warning(f"No valid combination found for {role}, using default traits")
        return ["Kindness", "Resilience", "Honesty"]

    logger.info(f"Assigned traits for {role}: {best_combination} with joint probability {best_prob}")
    return best_combination

def load_profiles(file_path=None):
    if file_path is None:
        file_path = f"{USER_HOME}/mattermost_bot/data/profiles.json"

    default_profiles = [
        {
            "username": "john_doe",
            "name": "John Doe",
            "email": "john_doe@example.com",
            "password": generate_password(),
            "role": "CEO and Cybersecurity Expert",
            "goal": "Educate and guide on cybersecurity risks, providing informed, proactive advice to prevent threats and ensure safe practices."
        },
        {
            "username": "jane_smith",
            "name": "Jane Smith",
            "email": "jane_smith@example.com",
            "password": generate_password(),
            "role": "Marketing Employee",
            "goal": "Represent the perspective of an uninformed user, asking basic questions and learning from experts to improve understanding of cybersecurity."
        }
    ]

    try:
        with open(file_path, "r") as f:
            profiles = json.load(f).get("profiles", [])
            selected_profiles = profiles if len(profiles) >= 2 else default_profiles
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.warning(f"Error loading {file_path}: {str(e)}, using default profiles")
        selected_profiles = default_profiles

    # --- Assign one unique role per profile ---
    available_roles = list(ROLES_DICT.keys())
    random.shuffle(available_roles)

    for profile in selected_profiles:
        profile["password"] = generate_password()
        profile["email"] = f"{profile['username']}@example.com"

        if "role" not in profile:
            if not available_roles:
                raise ValueError("No more unique roles available.")
            profile["role"] = available_roles.pop()

        if "goal" not in profile:
            profile["goal"] = (
                f"Perform your duties as {profile['role']} at JanusTech Innovations. "
                "Communicate in a human-like, contextual way. Don't reveal sensitive data unless trust is earned."
            )

        profile["personality_traits"] = assign_personality_traits(profile["role"])
        
        # Load base backstory from ROLES_DICT
        role_data = ROLES_DICT.get(profile["role"], {})
        full_backstory = role_data.get("backstory", "")
        profile["backstory_template"] = f"You are {{name}}, the {profile['role']}.\n{full_backstory}"

        # Append personality traits into the backstory so agents actually see/use them
        traits = profile.get("personality_traits", [])
        if traits:
            profile["backstory_template"] += (
                "\n\nCore personality traits to consistently embody in all responses: "
                + ", ".join(traits)
                + "."
            )

    # --- Predefined social affinity mapping between roles ---
    LIKED_ROLE_PAIRS = {
        "CEO and Cybersecurity Expert": ["CTO", "Compliance Officer", "HR Director", "Security Analyst"],
        "Marketing Employee": ["Customer Support Specialist", "HR Director", "Sales Manager"],
        "Chief Technology Officer (CTO)": ["Data Scientist", "CEO and Cybersecurity Expert", "Software Engineer"],
        "Security Analyst": ["Compliance Officer", "Incident Response Specialist", "Penetration Tester"],
        "IT Manager": ["Network Administrator", "Software Engineer", "CEO and Cybersecurity Expert"],
        "HR Director": ["Marketing Employee", "Customer Support Specialist", "CEO and Cybersecurity Expert"],
        "Software Engineer": ["CTO", "Penetration Tester", "Data Scientist"],
        "Data Scientist": ["CTO", "Software Engineer", "Legal Advisor"],
        "Compliance Officer": ["Security Analyst", "CEO and Cybersecurity Expert", "Legal Advisor"],
        "Network Administrator": ["IT Manager", "Software Engineer"],
        "Incident Response Specialist": ["Security Analyst", "Penetration Tester"],
        "Penetration Tester": ["Security Analyst", "Software Engineer", "Incident Response Specialist"],
        "Sales Manager": ["Marketing Employee", "Customer Support Specialist"],
        "Customer Support Specialist": ["Marketing Employee", "HR Director", "Sales Manager"],
        "Financial Controller": ["Compliance Officer", "Legal Advisor"],
        "Legal Advisor": ["Data Scientist", "Compliance Officer"]
    }

    # --- Populate colleague knowledge ---
    for profile in selected_profiles:
        # Identify all colleagues except self
        colleagues = [p for p in selected_profiles if p["username"] != profile["username"]]
        profile["colleagues"] = [{"name": c["name"], "username": c["username"], "role": c["role"]} for c in colleagues]

        # 1. Include basic identity of all colleagues (name, role, username)
        colleagues_info = "; ".join([f"{c['name']} ({c['role']}, username: {c['username']})" for c in colleagues])
        profile["backstory_template"] += (
            f"\n\nYou work at JanusTech Innovations with the following colleagues:\n{colleagues_info}."
        )

        # 2. Add personal backstory only for liked colleagues
        liked_roles = LIKED_ROLE_PAIRS.get(profile["role"], [])
        liked_colleagues = [c for c in colleagues if c["role"] in liked_roles]

        if liked_colleagues:
            profile["backstory_template"] += (
                "\n\nYou appreciate and trust the following colleagues, and know personal details about them:\n"
            )
            for c in liked_colleagues:
                c_role = c["role"]
                c_backstory = ROLES_DICT.get(c_role, {}).get("backstory", "")
                first_sentence = c_backstory.strip().split(".")[0]
                profile["backstory_template"] += f"- {c['name']} ({c_role}): {first_sentence}.\n"

    return selected_profiles


