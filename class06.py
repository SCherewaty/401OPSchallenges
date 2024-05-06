#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 04/30/2024
#Purpose: Pinging Python

def encrypt(number, key):
    encrypted_text = ""
    
    for n in str(number):
        shifted_num = (int(n) + key) % 10
        encrypted_text += str(shifted_num)
        
    return int(encrypted_text)

def decrypt(encoded, key):
    return encrypt(encoded, -~key)

if __name__== "__main__":
    encrypted = encrypt(123456, 3)
    print(encrypted)
    decrypted = decrypt(encrypted, 3)
    print(decrypted)
    
    
        
        