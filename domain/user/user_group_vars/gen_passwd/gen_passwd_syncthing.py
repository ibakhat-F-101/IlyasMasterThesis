import bcrypt
import xml.etree.ElementTree as ET
from common_utils import generate_strong_password, change_hash_in_vault

def hash_password(plaintext):
    salt = bcrypt.gensalt(rounds=10, prefix=b'2a')
    hashed = bcrypt.hashpw(plaintext.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def change_hash_in_config_xml(new_hash, file_path, username):
    tree = ET.parse(file_path)
    root = tree.getroot()

    gui = root.find('.//gui')
    if gui is not None:
        user = gui.find('user')
        if user is not None and user.text == username:
            password_element = gui.find('password')
            if password_element is not None:
                password_element.text = new_hash
                tree.write(file_path)

def change_password_syncthing(password, username='micropole_admin_944o4vj2'):
    ciphertext = hash_password(password)
    change_hash_in_vault(ciphertext, password, 'vault.yml', 'vault_syncthing_admin_password')
    change_hash_in_config_xml(ciphertext, '../syncthing/shared_folders/config/config.xml', username)

def main():
    password = generate_strong_password(8)
    change_password_syncthing(password)

if __name__ == "__main__":
    main()
