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
    


