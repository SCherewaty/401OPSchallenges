#!/usr/bin/python3

#Author: Steve Cherewaty
#Date: 06/12/2024
#Purpose: Signature based malware PART 3
#Sources: https://www.howtogeek.com/206097/how-to-use-find-from-the-windows-command-prompt/
# https://www.programiz.com/python-programming/examples/hash-file
# Conferred with Brad Baack, Omar Ardid and ChatGPT for this assignment

import os
import sys
import hashlib
import time
import requests
import threading

# Virustotal URL
API_URL = 'https://www.virustotal.com/api/v3/files/'

# FN search for a file in a directory
def search_file(file_name, search_directory, api_key):
    hits = 0  
    files_searched = 0  
# Store found files
    found_files = []  

    try:
# Walk through the directory tree
        for root, dirs, files in os.walk(search_directory):
            for file in files:
                files_searched += 1  
# Check if file_name (case insensitive) is in file (case insensitive)
                if file_name.lower() in file.lower():
                    hits += 1  
                    file_path = os.path.join(root, file)  
                    file_size = os.path.getsize(file_path)  
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  
                    md5_hash = generate_md5(file_path)  
                    print("")  
# Print file details
                    print(f"Timestamp: {timestamp}")
                    print(f"File: {file}")
                    print(f"Path: {file_path}")
                    print(f"Size: {file_size} bytes")
                    print(f"MD5: {md5_hash}")
                    print("-" * 40)  
# Check VirusTotal for file hash
                    positives = check_virustotal(md5_hash, api_key)  
                    if positives is not None:
# Print VirusTotal results
                        print(f"VirusTotal Positives: {positives}")  
                        detailed_report = check_virustotal(md5_hash, api_key, get_report=True)  
                        if detailed_report:
                            print(f"Detailed Report: {detailed_report}")  
                        else:
                            print(f"A detailed report is not available for {file} dude")
                    else:
# Handle UnicodeEncodeError by encoding to sys.stdout.encoding
                        encoded_hash = md5_hash.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
                        print(f"File not found on virustotal: {encoded_hash}")  
                    print("-" * 40)  
                    found_files.append((file, md5_hash, positives)) 
    except Exception as e:
# Handle unicode error in exception message
        encoded_error = str(e).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
        print(f"An error occurred: {encoded_error}") 
    
# Print search completion message
    print(f"\n Your search is complete. {files_searched} Here's what we searched. {hits} These are the hits found.")
 # Wait for user to press Enter
    input("\n Press Enter to exit.") 

# Function to generate the MD5 hash of a file
def generate_md5(file_path):
    hash_md5 = hashlib.md5()  
    try:
        with open(file_path, "rb") as f:  
# Open file in binary mode
            for chunk in iter(lambda: f.read(4096), b""):  
                hash_md5.update(chunk) 
    except Exception as e:
# Handle UnicodeEncodeError in exception message
        encoded_error = str(e).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
        print(f"Error reading file {file_path}: {encoded_error}")  
        return None
# Return MD5 hash digest as hexadecimal string 
    return hash_md5.hexdigest()  

def check_virustotal(file_hash, api_key, retries=3, get_report=False):
    headers = {
        'x-apikey': api_key  
    }
# Construct API URL with file hash
    url = f'{API_URL}{file_hash}'  
    for attempt in range(retries): 
# Send GET request to VirusTotal API
        response = requests.get(url, headers=headers) 
# If successful response 
        if response.status_code == 200:  
            result = response.json() 
            if 'data' in result and 'attributes' in result['data']:
                if get_report:
# Get detailed report URL from Virustotal
                    detailed_report_url = result['data']['attributes'].get('last_analysis_results', {}).get('verbose_msg', 'No detailed report available')
                    return detailed_report_url 
                else:
# Get number of malicious detections from Virustotal
                    positives = result['data']['attributes'].get('last_analysis_stats', {}).get('malicious', 0)
# Return number of positives
                    return positives  
            else:
                print(f"No Virustotal results for {file_hash}")  
                return None 
# If rate limit exceeded
        elif response.status_code == 204:  
            print(f"Rate limit exceeded. Retrying in 15 seconds...") 
# Wait 15 seconds before retrying 
            time.sleep(15)  
# If file not found on Virustotal
        elif response.status_code == 404:  
            return None  
        else:
            print(f"Error querying Virustotal: {response.status_code}")  
            return None  
    return None  # Return None if retries exhausted

# Function to prompt for Virustotal API key
def prompt_for_api_key():
# Prompt user for API key
    api_key = input("Enter your Virustotal API key: ").strip()  
    if not api_key:  
        print("YO! API key cannot be empty. Please provide a valid Virustotal API key.") 
# Recursively prompt for API key
        return prompt_for_api_key()  
    return api_key  

# Main function
def main():
# Get current operating system
    operating_system = sys.platform  
    if operating_system.startswith('linux') or operating_system.startswith('win32'):
        (f"Running on {operating_system.capitalize()}")  
# Prompt user for file name
        file_name = input("Enter the file name to search for: ")  
        search_directory = input("Enter the directory to search in: ")  
        if not os.path.exists(search_directory): 
# Handle Unicode error in directory not found message
            encoded_error = f"The specified directory '{search_directory}' doesn't exist.".encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
            print(f"{encoded_error}") 
            return 
    else:
        print("You got an unsupported operating system.")  
        return  

# Prompt user for Virustotal API key
    api_key = os.getenv('API_KEY_VIRUSTOTAL')  
# If API key is not set
    if not api_key:  
        api_key = prompt_for_api_key()  
        os.environ['API_KEY_VIRUSTOTAL'] = api_key 
# Create search thread
    search_thread = threading.Thread(target=search_file, args=(file_name, search_directory, api_key))  
    search_thread.start()  
    search_thread.join()  

if __name__ == "__main__":
    main()  
    
# End