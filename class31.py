#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 06/10/2024
#Purpose: Signature based malware PART 1
#Sources: https://www.howtogeek.com/112674/how-to-find-files-and-folders-in-linux-using-the-command-line/
# https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/
# 

import os
import platform

def search_files(filename, search_directory):
    file_count = 0
    hit_count = 0

    for root, dirs, files in os.walk(search_directory):
        file_count += len(files)
        for name in files:
            if name == filename:
                hit_count += 1
                print(f"File found: {os.path.join(root, name)}")
    print(f"\nTotal files searched: {file_count}")
    print(f"Total hits found: {hit_count}")

if __name__ == "__main__":
    filename = input("Enter the file name to search for: ")
    search_directory = input("Enter the directory to search in: ")

    # Normalize the directory path
    search_directory = os.path.normpath(search_directory)

    # Verify if the directory exists
    if not os.path.isdir(search_directory):
        print(f"Error: The directory {search_directory} does not exist.")
    else:
        # Check the operating system
        current_os = platform.system()
        print(f"Current operating system: {current_os}")


