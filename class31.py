#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 06/10/2024
#Purpose: Signature based malware PART 1
#Sources: 
# Worked with Brad Baack on this Ops Challenge

import time  # Import time module for delays
import getpass  # Import getpass module to securely get user passwords
import os  # Import os module for file system operations
import paramiko  # Import paramiko for SSH connections
import zipfile  # Import zipfile for handling zip files
import logging  # Import logging module
from logging.handlers import RotatingFileHandler  # Import RotatingFileHandler for log rotation

# [MOD] Configure logging with rotation, file, and stream handlers
def setup_logger(log_file):
    logger = logging.getLogger("BruteForceLog")
    logger.setLevel(logging.DEBUG)
    
    # [MOD] Add a rotating handler
    rotating_handler = RotatingFileHandler(log_file, maxBytes=2000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rotating_handler.setFormatter(formatter)
    
    # [MOD] Add a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    # [MOD] Add a stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    
    # [MOD] Add handlers to the logger
    logger.addHandler(rotating_handler)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    
    return logger

# [MOD] Setup logger
logger = setup_logger('brute_force.log')

# Function to read lines from a file with optional delay
def read_file(filepath, delay=0):
    if not os.path.isfile(filepath):  # Check if the file exists
        logger.error(f"File not found: {filepath}")  # [MOD] Log file not found error
        return None
    with open(filepath, encoding="ISO-8859-1") as file:  # Open file with specified encoding
        for line in file:
            yield line.rstrip()  # Remove trailing whitespace and yield the line
            if delay:
                time.sleep(delay)  # Delay for specified time if delay is set

# Function to iterate through words in a dictionary file
def iterator():
    filepath = input("Enter your dictionary filepath:\n") or "rockyou.txt"
    for word in read_file(filepath, delay=1):  # Read file with 1-second delay between lines
        if word is None:
            return
        logger.info(f"Read word: {word}")  # [MOD] Log each word read
        print(word)

# Function to check if a password is in a dictionary file
def check_password():
    usr_password = getpass.getpass(prompt="Please enter a password: ")
    usr_filepath = input("Enter a dictionary filepath:\n") or "rockyou.txt"
    wordlist = list(read_file(usr_filepath))  # Read file into a list
    if wordlist is None:
        return

    if usr_password not in wordlist:  # Check if password is not in wordlist
        logger.info("Password is acceptable.")  # [MOD] Log acceptable password
        print("Your password is acceptable. Good job.")
    else:
        logger.warning("Password found in dictionary.")  # [MOD] Log password found in dictionary
        print("Your password was found in the dictionary. Please choose another password.")
