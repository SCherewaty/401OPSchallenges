#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 04/30/2024
#Purpose: Encrypting in Python
#Sources: https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
#         https://cryptography.io/en/latest/

from cryptography.fernet import Fernet

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
            

 

#ALTERNATE CODE - I tried this but it was so wildly different and I don't know enough to know if it's usable...
# from cryptography.fernet import Fernet
# key = Fernet.generate_key()

# with open("401class2A.py", 'rb') as file:
#     data = file.read()
    
# # Encrypt the data
# Fernet = Fernet(key)
# encrypted_data = Fernet.encrypt(data)

# with open("401class2A_encrypted.py", 'wb') as encrypted_file:
#     encrypted_file.write(encrypted_data)


    
    
        
        