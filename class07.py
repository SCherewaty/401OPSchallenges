#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/07/2024
#Purpose: Recursive Encrypting
#Sources: https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
#         https://cryptography.io/en/latest/


import subprocess
from cryptography.fernet import Fernet
import os

# Encrypt a file 
def write_key():
    key = Fernet.generate_key()
    with open("Crypt.key", "wb") as key_file:
        key_file.write(key)
        
    def load_key():
        return open("Crypt.key", "rb").read()
    
    def encrypt_file(file_path, key):
        try:
            f = Fernet(key)
            with open(file_path, "rb") as file:
                file_data = file.read()
            encrypted_data = f.encrypt(file_data)
            with open(file_path, "wb") as file:
                file.write(encrypted_data)
            print("File was encrypted!")
        except Exception as e:
            print(f"file NOT encrypted: {e}")
            
# DEcrypt a file 
def decrypt_file(file_path, key):
   
        try:
            f = Fernet(key)
            with open(file_path, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
            with open(file_path, "wb") as file:
                file.write(decrypted_data)
            print("File was decrypted!")
        except FileNotFoundError:
            print(f"Error: Encrypted file '{file_path}' not found")
            
#Create loop for modes
while True:
    print("~~~~ Encrypting and Decrypting MENU ~~~~")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Exit")
    choice = input("Before running this script make sure to have 'cryptography' installed./Enter your choice: ").lower()
    if choice == '1':
        write_key()
        key = load_key()
        file_path = input("Enter the name of the path to encrypt:")
        encrypt_file(file_path, key)
    elif choice == '2':
        if key is None:
            print("Error: Please encrypt a file (option 1) to generate the key.")
            continue
        file_path = input("Enter the file path to decrypt: ")
        decrypt_file(file_path, key)
    elif choice == '3':
        write_key()
        key = load_key()
        message = input("Enter a message to encrypt: ").encode()
        fernet = Fernet(key)
        encrypted_message = fernet.encrypt(message)
        print("Encrypted message:", encrypted_message)
    elif choice == '4':
        key = load_key()
        encrypted_message = input("Enter the encrypted message: ")
        fernet = Fernet(key)
        try:
            decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
            print("Decrypted message:", decrypted_message)
        except Exception as e:
            print(f"Error decrypting message: {e}")
    elif choice == '6':
        print ("Thank you, goodbye.")
        break
    else:
        print("Choose more wisely")