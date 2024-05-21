#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/20/2024
#Purpose: Iterate over a set
#Sources: https://www.geeksforgeeks.org/iterate-over-a-set-in-python/
# Worked with Brad Baack and Cody Blahnik on this challenge

# Import the correct libraries
import time
import getpass
import os

# Bring in and define function
def iterator():
    filepath = input("Enter the dictionary filepath:\n") or "rockyou.txt" 
    if not os.path.isfile(filepath):  
        print(f"File not found: {filepath}")  
# Print error message if file not found
        return  
    
# Open the file
    file = open(filepath, encoding="ISO-8859-1")   
    line = file.readline()  
    while line:  
        line = line.rstrip()  
        word = line  
        print(word)  
# Print word
        time.sleep(1)  
        line = file.readline()  
    file.close() 
        
        
def check_password():
    usr_password = getpass.getpass(prompt="Please enter a password: ") 
# Prompt user for file path, default to 'rockyou.txt'
    usr_filepath = input("Strength-o-meter for this password.\nPlease enter a dictionary filepath:\n") or "rockyou.txt"  
  
# Check if the file exists
    if not os.path.isfile(usr_filepath):  
        print(f"File not found: {usr_filepath}")  
        return  
    
    print(f"Checking password against the words in '{usr_filepath}', just a moment.")  
    t1 = time.time()  
    file = open(usr_filepath, encoding="ISO-8859-1")  
    line = file.readline()  
    wordlist = []  
# Loop until no more lines in the file
    while line:  
        line = line.rstrip() 
        word = line  
        wordlist.append(word)  
        line = file.readline()  
    file.close()  
# Check if the password is not in the wordlist  
    if usr_password not in wordlist:  
        print("Your password is okay.")  
    else:
        print("Your password is forbidden. Try another.")  
    t2 = time.time()  # Record the end time
    print(f"Password check completed in {t2 - t1:.2f} seconds.")  
    
#Main 
     
if __name__ == "__main__":  
    
# Start an infinite loop
    while True:  
        print("\nBrute Force Wordlist Attack Tool Menu") 
        print("1 - Offensive, Dictionary Iterator")  
        print("2 - Defensive, Password Recognized") 
        print("3 - Exit") 
# Get user input for menu option        
        mode = input("Please enter a number: ")  
        
        if mode == "1":
            iterator()  
        elif mode == "2":
            check_password()  
        elif mode == "3":
            break  
        else:
            print("Invalid selection...")             
   
 #end         
    
    

    

   

