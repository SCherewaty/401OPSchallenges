#!/usr/bin/env python3

#Author: Steve Cherewaty
#Date: 06/19/2024
#Purpose: XSS Vulnerability Detection with Python
#Sources: 
# 
# https://thepythoncode.com/article/make-a-xss-vulnerability-scanner-in-python
# Conferred with ChatGPT for this assignment

# Author:      Abdou Rockikz
# Description: A script to detect XSS vulnerabilities in web forms by injecting a payload and checking the response.
# Date:        TODO: 06/20/2024
# Modified by: TODO: Steve Cherewaty

# Make sure to install requests and bs4 before executing this in Python3
# You can install them using pip:
# pip3 install requests bs4

# Import libraries
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Function to get all forms from a URL
# This function fetches the HTML content of the given URL, parses it, and returns all form tags found.
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# Function to extract details of a form
# This function takes a form element as input and extracts its action URL, method, and input fields.
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# Function to submit a form with a given payload
# This function constructs a full URL from the form's action attribute and the base URL, fills the form inputs with a given value (payload), and submits it.
def submit_form(form_details, url, value):
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### This function scans a URL for XSS vulnerabilities by submitting forms with a test script ###
### It checks if the test script is executed in the response, indicating an XSS vulnerability ###
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script>alert('XSS')</script>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### This is the entry point of the script ###
### It prompts the user for a URL, scans it for XSS vulnerabilities, and prints the results ###
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### Tested Outputs ###
### Positive Detection Output:
# Enter a URL to test for XSS: http://example.com/vulnerable
# [+] Detected 1 forms on http://example.com/vulnerable.
# [+] XSS Detected on http://example.com/vulnerable
# [*] Form details:
# {'action': 'process.php', 'method': 'post', 'inputs': [{'type': 'text', 'name': 'query'}]}

### Negative Detection Output:
# Enter a URL to test for XSS: http://example.com/safe
# [+] Detected 1 forms on http://example.com/safe.
# No XSS Detected on http://example.com/safe
# End