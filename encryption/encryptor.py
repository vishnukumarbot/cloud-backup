from cryptography.fernet import Fernet
import os

key_file = "config/encryption_key.key"

def generate_key():
    # Ensures the config directory exists
    os.makedirs("config", exist_ok=True)

    # Generates and save the key
    key = Fernet.generate_key()
    with open(key_file, "wb") as file:
        file.write(key)
    print(f"Encryption key generated and saved to {key_file}")

def load_key():
    # Checks if the key file exists
    if not os.path.exists(key_file):
        raise FileNotFoundError(f"Encryption key not found. Run 'generate_key' first to create {key_file}")
    with open(key_file, "rb") as file:
        return file.read()

def encrypt_file(file_path):
    cipher = Fernet(load_key())
    with open(file_path, "rb") as file:
        encrypted_data = cipher.encrypt(file.read())
    encrypted_file_path = f"{file_path}.enc"
    with open(encrypted_file_path, "wb") as file:
        file.write(encrypted_data)
    return encrypted_file_path

if __name__ == "__main__":
    import sys

    # Checks for command-line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "generate_key":
        generate_key()
    else:
        print("Usage: python -m encryption.encryptor generate_key")
