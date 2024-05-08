#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/07/2024
#Purpose: Recursive Encrypting (Part 2)
#Sources: https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/
#         https://stackoverflow.com/questions/62848017/using-python-cryptography-module-to-encrypt-recursively


#Import Fernet
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
    
   if mode == '1':
       file_path = input("Enter file path: ")
       if os.path.exists(file_path):
           encrypt_file(file_path)
           print("File is encrypted!")
       else:
           print("File not found.")
    elif mode =='2':
        file_path = input("Enter file path: ")
       if os.path.exists(file_path):
           decrypt_file(file_path)
           print("File is decrypted!")
       else:
           print("File not found.")
     elif mode =='3':
        folder_path = input("Enter folder path: ")
       if os.path.exists(folder_path):
           encrypt_file(folder_path)
           print("Folder is encrypted and contents exposed!")
       else:
           print("Folder not found.")
    elif mode =='4':
        folder_path = input("Enter folder path: ")
       if os.path.exists(folder_path):
           decrypt_file(folder_path)
           print("Folder is decrypted and contents locked down!")
       else:
           print("Folder not found. ")
    else:
        print("Error: invalid entry. ")
        
if __name__ == "__main__":
    main()
    
#end