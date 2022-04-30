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
        print("OK")
        print(line)
        print(r.text)
        print(r.status_code)
    else:
        print("FAIL")
        print(line)
        print(r.status_code)

# close file without changes
urls.close()