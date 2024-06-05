#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 06/04/2024
#Purpose: Logging
#Sources: 

#Import Libraries
import time  
import getpass  
import os  
import paramiko 
import zipfile  
import logging
from logging.handlers import RotatingFileHandler

# Set up logging with rotation
log_handler = RotatingFileHandler('brute_force.log', maxBytes=5*1024*1024, backupCount=3)  
log_handler.setLevel(logging.DEBUG)
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(format)
  
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(log_handler)

#def iterator():
# Prompt user for file path, default to 'rockyou.txt'
    #filepath = input("Enter your dictionary filepath:\n") or "rockyou.txt"  

# Function to read lines from a file with optional delay
def read_file(filepath, delay=0):
    if not os.path.isfile(filepath):  
        logger.error(f"File not found: {filepath}")  
        return None
    with open(filepath, encoding="ISO-8859-1") as file:  
        for line in file:
            yield line.rstrip()  
            if delay:
                time.sleep(delay)  
 
 # Function to iterate through words in a dictionary file
def iterator():
    filepath = input("Enter your dictionary filepath:\n") or "rockyou.txt"
    for word in read_file(filepath, delay=1):  # Read file with 1-second delay between lines
        if word is None:
            return
        logger.info(f"Read word: {word}")  # [MOD] Log each word read
        print(word)
 

def check_password():
    usr_password = getpass.getpass(prompt="Please enter a password: ") 
# Prompt user for file path, default to 'rockyou.txt' 
    usr_filepath = input("Checking the strength of that password.\nPlease enter a dictionary filepath:\n") or "rockyou.txt"  

    if not os.path.isfile(usr_filepath): 
        print(f"File not found: {usr_filepath}")  
        return  
    
    print(f"Checking password against the words in '{usr_filepath}', hang on for a sec.") 
    t1 = time.time()  
    file = open(usr_filepath, encoding="ISO-8859-1") 
    line = file.readline()  
    wordlist = []  
    while line:  
        line = line.rstrip()  
        word = line  
        wordlist.append(word)  
        line = file.readline()  
    file.close()  
    
 # Check if the password is not in the wordlist   
    if usr_password not in wordlist:  
        print("Your password is acceptable. Good job.")  
    else:
        print("Your password was found in the dictionary. Try again...you have 10 seconds...")  
    t2 = time.time()  
    # Print the duration of the check
    print(f"Password check completed in {t2 - t1:.2f} seconds.")  

def brute_force_ssh():
    ip = input("Enter the target IP address:\n")
    username = input("Enter the SSH username:\n")
    filepath = input("Enter your dictionary filepath:\n") or "rockyou.txt"
    
    if not os.path.isfile(filepath):
        print(f"File not found: {filepath}")
        return
    
    file = open(filepath, encoding="ISO-8859-1")
    line = file.readline()
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    
    
 #  Prompt user for path to zip file 
def extract_zip():
    zip_file = input("Enter the path of the zip file:\n")
    if not os.path.isfile(zip_file):
        print (f"FIle not found: {zip_file}")
        return
# Prompt usr for file path or rockyou
    dictionary_path = input("Enter your dictionary filepath:\n") or "rockyou.txt"
    if not os.path.isfile(dictionary_path):
        print(f"File not found: {dictionary_path}")
        return

    with ZipFile(zip_file) as zf:
        with open(dictionary_path, encoding="ISO-8859-1") as file:
            for line in file:
                password = line.strip()
                try:
                    zf.extractall(pwd=bytes(password, 'utf-8'))
                    print(f"Success! Password: {password}")
                    return
                except RuntimeError:
                    print(f"Failed: {password}")
                except Exception as e:
                    print(f"Error: {e}")
                    return
    print("No valid password found in the dictionary.")


# Main
if __name__ == "__main__":  
# Start an  loop
    while True:  
        print("\nBrute Force Wordlist Attack Tool Menu")  
        print("1 - Offensive, Dictionary Iterator")  
        print("2 - Defensive, Password Recognized")  
        print("3 - Offensive, SSH Brute Force") 
        print("4 - Offensive, Zip Brute Force ") 
        print("5 - Exit") 
         
# Get user input for menu option
        mode = input("Please enter a number: ")  
        
        if mode == "1":
            iterator()  
        elif mode == "2":
            check_password() 
        elif mode == "3":
            brute_force_ssh() 
        elif mode == "4":
            extract_zip()
        elif mode == "5":
            break  
        else:
            print("Invalid selection...") 