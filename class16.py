#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 05/20/2024
#Purpose: Natural language toolkit
#Sources: 

# Import ssl and natural language toolkit
import ssl
import nltk
from nltk.corpus import words

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
    
# Download natural language toolkit
def get_words():
    nltk.download('words')
# Assign variable
    word_list = words.words()
    return word_list
    
# Prompt the user for a string
def check_for_word(words):  
    user_answer = input("Enter a word")
    if user_answer in words:
        print("The word is in the dictionary")
    else:
        print("The word is NOT in the dictionary")
    

    
if __name__ == "__main__":
    #call the word_list variable
    external_words = get_words()
   #print(external_words)
   

