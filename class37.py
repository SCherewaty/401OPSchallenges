#!/usr/bin/env python3

#Author: Steve Cherewaty
#Date: 06/18/2024
#Purpose: Cookies
#Sources: https://www.dev2qa.com/how-to-get-set-http-headers-cookies-and-manage-sessions-use-python-requests-module/#google_vignette
# Conferred with ChatGPT for this assignment

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests
import webbrowser
import os

targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Send back to site to get a response
response_with_cookie = requests.get(targetsite, cookies=cookie)

# Capture contents of response
html_content = response_with_cookie.text
html_filename = "response.html"

with open(html_filename, "w") as file:
    file.write(html_content)
    
# Open the file with Firefox
firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe" # Adjust the path if necessary
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
webbrowser.get('firefox').open('file://' + os.path.realpath(html_filename)) 

# End