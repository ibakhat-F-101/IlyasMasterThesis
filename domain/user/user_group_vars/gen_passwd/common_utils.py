import os
import shutil
import subprocess


def change_hash_in_vault(new_hash, cleartext, vault_file, label):

    with open(vault_file, 'r') as file:
        vault_data = file.read()

    updated_data = update_hash_vault_data(vault_data, new_hash, cleartext, label)
    
    with open(vault_file, 'w') as file:
        file.write(updated_data)

def update_hash_vault_data(vault_data, new_hash, cleartext, label):
    lines = vault_data.split('\n')
    for i, line in enumerate(lines):
        if line.startswith(f'{label}:'):
            lines[i - 1] = f'# Cleartext: {cleartext}' if i > 0 and lines[i - 1].strip().startswith('# Cleartext:') else f'# Cleartext: {cleartext}'
            lines[i] = f'{label}: {new_hash}'
            break
    return '\n'.join(lines)

def clear_temp_directory(temp_dir):
    for item in os.listdir(temp_dir):
        item_path = os.path.join(temp_dir, item)
        if item != '.gitkeep':
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)

def generate_strong_password(number_of_words=8, length=32):
    command = [
        'diceware',
        '--num', str(number_of_words),
        '--no-caps',
        '--delimiter', '-',
        '--wordlist', 'en_eff'
    ]
    
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error generating password: {e.stderr}")
        return None
