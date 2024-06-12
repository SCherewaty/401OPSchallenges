#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 06/11/2024
#Purpose: Signature based malware PART 2
#Sources: https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/
# https://www.programiz.com/python-programming/examples/hash-file


import os
import platform
import hashlib
import time

def generate_md5(file_path):
    """Generate the MD5 hash for the given file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except IOError:
        return "Error reading file"

def search_files_and_folders(search_directory):
    total_items_count = 0

for root, dirs, files in os.walk(search_directory):
        for name in dirs + files:
            item_path = os.path.join(root, name)
            total_items_count += 1
            
            if os.path.isfile(item_path):
                file_size = os.path.getsize(item_path)
                md5_hash = generate_md5(item_path)
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(os.path.getmtime(item_path)))
                    
            print(f"Timestamp: {timestamp}")
            print(f"File Name: {name}")
            print(f"File Size: {file_size} bytes")
            print(f"File Path: {item_path}")
            print(f"MD5 Hash: {md5_hash}\n")
        else:
            print(f"Directory: {item_path}")

        print(f"\nTotal items (files and directories) found: {total_items_count}")

if __name__ == "__main__":
    search_directory = input("Enter the directory in which you want to search: ")



    # Normalize the directory path
    search_directory = os.path.normpath(search_directory)

    # Verify if the directory exists
    if not os.path.isdir(search_directory):
        print(f"Error: The directory {search_directory} does not exist.")
    else:
        # Check the operating system
        current_os = platform.system()
        print(f"Current operating system: {current_os}")
        
        search_files_and_folders(filename, search_directory)
          
# End


