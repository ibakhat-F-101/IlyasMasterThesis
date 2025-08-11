from passlib.hash import bcrypt_sha256
from common_utils import generate_strong_password, change_hash_in_vault
import crypt
"""
The goal of this script is to generate a strong password for the Bitwarden user (the one on the VM ! NOT the one on the Bitwarden website !) and put it in the Ansible-vault file, so it is not visible in the repo.
"""

def hash_password(password):
    return (crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512)))

def verify_password(plaintext, ciphertext):
    salt = ciphertext[:ciphertext.rfind('$')+1]
    hashed_plaintext = crypt.crypt(plaintext, salt)
    return hashed_plaintext == ciphertext
    
##### Tests #####
def test_hash_password():
    password = "example_password"
    hashed = hash_password(password)
    assert bcrypt_sha256.verify(password, hashed)

def test_verify_password():
    password = "example_password"
    hashed = hash_password(password)
    assert verify_password(password, hashed)
##### \ Tests #####


def change_password_bitwarden(password):
    ciphertext = hash_password(password)
    print(ciphertext)
    print(verify_password(password, ciphertext))
    if verify_password(password, ciphertext):
        print("Password verified!")
        change_hash_in_vault(ciphertext, password, 'vault.yml', 'vault_user_password_bitwarden')
    else:
        print("Password verification failed!")

def main():
    password = generate_strong_password(8)
    print("Generated password for Bitwarden:", password)

    change_password_bitwarden(password)

if __name__ == "__main__":
    main()
 
            
