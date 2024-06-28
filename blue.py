#!/usr/bin/env python3

#Author: Steve Cherewaty
#Date: 06/28/2024

import subprocess
import logging
import readline
import os

# Configure logging
logging.basicConfig(filename='pentest_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def execute_command(command):
    try:
        logging.info(f"Executing command: {command}")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        logging.info(f"Command output: {result.stdout}")
        logging.error(f"Command error (if any): {result.stderr}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Command '{command}' failed with error: {e}")
        return e.stderr

def main():
    while True:
        command = input("Enter the command to execute: ")
        if command.lower() in ["exit", "quit"]:
            logging.info("Exiting the script.")
            break
        logging.info(f"Current directory: {os.getcwd()}")
        output = execute_command(command)
        print(output)

if __name__ == "__main__":
    main()