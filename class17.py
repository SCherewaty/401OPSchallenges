#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/21/2024
#Purpose: Brute Force II
#Sources: 

import time
import paramiko, os, sys, socket

def offensive():
    wordlistpath = input("Enter file path: ")
    if os.path.isfile(wordlistpath):
        try:
            with open(wordlistpath):
                for word in wordlistfile:
                    word = word.rstrip()
                    print(word)
                    time.sleep(0.1)
                    
        except Exception as e:
            print(f"An error has occurred: {e}")
    else:
        print("Word file not found.  Enter a valid file path. ")
        
