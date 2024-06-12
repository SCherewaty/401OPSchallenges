#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 06/11/2024
#Purpose: Signature based malware PART 2
#Sources: https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/
# https://www.programiz.com/python-programming/examples/hash-file
# Conferred with Omar Ardid and ChatGPT for this assignment

import os
import sys
import hashlib
import time

# Function to search for a file in a directory
def search_file(file_name, search_directory):
    # Initialize counters
    hits = 0
    files_searched = 0

    try:
        # Traverse directory and search for files
        for root, dirs, files in os.walk(search_directory):
            for file in files:
                files_searched += 1
                # Check if file name contains the specified search term
                if file_name.lower() in file.lower():
                    hits += 1
                    file_path = os.path.join(root, file)
                    # Get the file size
                    file_size = os.path.getsize(file_path)
                    # Get the current timestamp
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    # Generate the MD5 hash of the file
                    md5_hash = generate_md5(file_path)
                    # Print the file details
                    print(f"Timestamp: {timestamp}")
                    print(f"File: {file}")
                    print(f"Path: {file_path}")
                    print(f"Size: {file_size} bytes")
                    print(f"MD5: {md5_hash}")
                    print("-" * 40)
                    
# Handle exceptions
    except Exception as e:
        print(f"YO! An error occurred: {str(e)}")

 # Print search summary
    print(f"\n Search completed. {files_searched} files searched. {hits} hits found.")
    # Wait for user input before exiting
    input("\n Press Enter to exit.")

# Function to generate the MD5 hash of a file
def generate_md5(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except Exception as e:
        print(f"Oh no! Error reading file {file_path}: {str(e)}")
        return None
    return hash_md5.hexdigest()

# Main
def main():
    """Generate the MD5 hash for the given file."""
    operating_system = sys.platform
    print(operating_system)
    if operating_system.startswith('linux') or operating_system.startswith('mac'):
        file_name = input("Enter the file name you want to search for Homie: ")
        search_directory = input("Enter the directory to search in Bro: ")
            
        if not os.path.exists(search_directory):
            print("That directory doesnt exist...trust me I'm a robot.")
            return
    else:
        print("We don't support that OS.")
        return
                 
    search_file(file_name, search_directory)    

if __name__ == "__main__":
    main()



          
# End


