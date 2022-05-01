from encodings import utf_8
import time
import hashlib
import os
import requests
#from urllib import response
#from urllib.request import urlopen, Request

# open file that contains URLs to check
urls = open('urls.txt')

# check URLs for response code, then check for contents
lines = urls.readlines()
for line in lines:
    r = requests.get(line)
    if r.status_code == 200:
        # below commented lines are for testing purposes
        # print("OK")
        # print(line)
        # print(r.text)
        # txt = r.text
        print(r.status_code)
        hash_object = hashlib.sha256(r.text.encode())
        print(hash_object.hexdigest())
    else:
        print("Fetching from " + line + " has FAILED!")
        # below commented lines are for testing purposes
        # print(line)
        # print(r.status_code)

# close file without changes
urls.close()

