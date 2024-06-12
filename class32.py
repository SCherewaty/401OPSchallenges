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
        file_count += len(files)
        for name in files:
            if name == filename:
                hit_count += 1
                print(f"Your file was found: {os.path.join(root, name)}")
    print(f"\nTotal files searched: {file_count}")
    print(f"Total hits found: {hit_count}")
    
if __name__ == "__main__":
    search_directory = input("Enter the directory in which you want to search: "

# if __name__ == "__main__":
#     filename = input("Enter the name of the file you wish to search for: ")
#     search_directory = input("Enter the directory in which you want to search: ")

    # Normalize the directory path
    search_directory = os.path.normpath(search_directory)

    # Verify if the directory exists
    if not os.path.isdir(search_directory):
        print(f"Error: The directory {search_directory} does not exist.")
    else:
        # Check the operating system
        current_os = platform.system()
        print(f"Current operating system: {current_os}")
        
        search_files(filename, search_directory)
          
# End


