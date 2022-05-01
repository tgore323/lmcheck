from encodings import utf_8
import time
import hashlib
import os
import requests


# open file that contains URLs to check and create list for hash values
urls = open('urls.txt')
'''
or, you can just put the URLs in a list
# urls = ['https://mirror.crexio.com/linuxmint/isos/testing/sha256sum.txt', 
# 'https://ftp.crifo.org/mint-cd/testing/sha256sum.txt']
'''
hash_list = []

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
        store = hash_object.hexdigest()
        hash_list.append(store)
    else:
        print("Fetching from " + line + " has FAILED!")
        # below commented lines are for testing purposes
        # print(line)
        # print(r.status_code)

# close file without changes
urls.close()
#print(store)
#print(hash_list)

# saves hash values to hidden tmp file for comparison
temp = open('.tmp.txt', 'w+')
for h in hash_list:
    temp.write(h + '\n')

# checks for tmp file. if it exists, compare contents
if os.path.isfile('.tmp.txt') == True:
    open('.tmp.txt', 'w+')
    # create a list with each line in tmp file, then compare
    before = []
    after = []
    if before == after:
        print("No changes detected")
    else:
        print("Changes detected")