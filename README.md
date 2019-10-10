# Check-Mal-URL

Quick script I came up with to analyze a suspicious/malicious URL that you may come across. First, the script will check to ensure the site returns a HTTP status code of 200. 

Next, the script will check for the existence of any script or iframe tags and print them. 

*NOTE* Most malicious actors will use some sort of obfuscation techniques to hide their malicious code. This script does not currently check for/decode any obfuscation techniques. This will hopefully be added later.

This was more of a project to assist in learning and assist me to take a quick look at a URL as I research different subjects in my lab. 
