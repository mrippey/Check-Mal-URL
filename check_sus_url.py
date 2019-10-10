#!/usr/bin/env python3
#
# check_sus_ur.py

# Author: Mike R.
#
# Twitter: @nahamike01

import requests
import sys
from bs4 import BeautifulSoup

'''
Purpose: Take in a suspect URL and check if the site is still up.  
Additionally, The site will use BeautifulSoup to parse the HTML &
print out any script or iframe tags found.  

TODO: Check for input that is not a valid URL
      Attempt to identify obfuscated iframe/script tags
      Submit input to analysis API??
'''
if len(sys.argv) < 2:
    print(sys.argv[0] + "url path")

response = requests.get(sys.argv[1])
if response.status_code != 200:
    print("failed to connect")
    sys.exit(1)
else:
    print(f'status code: {response.status_code} ')

input("Press <ENTER> key to continue to HTML output...")

plain_txt = response.text
soup = BeautifulSoup(plain_txt, 'html.parser')

for scr in soup.find_all(text=lambda l: l and any(x in l for x in ['iframe', 'script'])):
    print(scr)
else:
    print("No scripts found! Further analysis may be required for obfuscated code.")
