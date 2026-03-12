# Import Required Module
from cryptography.fernet import Fernet
import os


# Key Management 

# Check if key already exists
if os.path.exists("secret.key"):
    # Load existing key
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
else:
    # Generate new key
    key = Fernet.generate_key()

    # Save key in file
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

cipher = Fernet(key)

print("Encryption Key Loaded Successfully")


# Menu

print("\nChoose Option")
print("1. Encrypt Text")
print("2. Decrypt Text")

choice = input("Enter choice (1 or 2): ")


#Encrypt Option

if choice == "1":

    text = input("Enter text to encrypt: ")

    encrypted_text = cipher.encrypt(text.encode())

    print("\nEncrypted Text:")
    print(encrypted_text.decode())


# Decrypt Option

elif choice == "2":

    encrypted_input = input("Enter encrypted text: ")

    try:
        decrypted_text = cipher.decrypt(encrypted_input.encode())

        print("\nDecrypted Text:")
        print(decrypted_text.decode())

    except:
        print("Invalid encrypted text or wrong key!")


# Invalid Option

else:
    print("Invalid Choice")
