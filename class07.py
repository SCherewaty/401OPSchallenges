#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/07/2024
#Purpose: Recursive Encrypting (Part 2)
#Sources: 


import subprocess
from cryptography.fernet import Fernet
import os

# Generate a key
key = Fernet.generate_key()
   
#Cipher Suite
cipher_suite = Fernet(key)

#Encrypt a file
def encrypt_file(file_path):
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    encrypted_text = cipher_suite.encrypt(plaintext)
    with open(file_path, 'wb') as f:
        f.write(encrypted_text)
        
#Decrypt a file
def decrypt_file(file_path):
    with open(file_path, 'rb') as f:
        encrypted_text = f.read()
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    with open(file_path, 'wb') as f:
        f.write(decrypted_text)    
        
#Recursive encryption for folder
def encrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path)
            
#Recursive decryption for folder
 def decrypt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path)      
            

#Create mode options
def main():
    print("~~~~ Choose a mode ~~~~")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a folder")
    print("4. Decrypt a folder")
    print("5. Exit")
    
    mode = input("enter mode: ")
    
   