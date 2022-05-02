from encodings import utf_8
# import time
import hashlib
import os
import requests


# open file that contains URLs to check and create list for hash values
urls = open('urls.txt')
tmp = open('.tmp.txt')

old = []
new = []
hash_list = []

# check URLs for response code, if 200, hash the sha256sum.txt file
lines = urls.readlines()
for line in lines:
    r = requests.get(line)
    if r.status_code == 200:
        hash_object = hashlib.sha256(r.text.encode())
        store = hash_object.hexdigest()
        new.append(store)
    else:
        print("Fetching from " + line + " has FAILED!")

# close the list of URLs
urls.close()



# saves hash values to hidden tmp file for comparison
temp = open('.tmp.txt', 'w+')
for h in hash_list:
    temp.write(h + '\n')

# checks for tmp file. if it exists, compare contents
# tmp = old
temps = tmp.readlines()
for temp in temps:
    old.append(temp)

print('new hash is: ')
print(new)
print('old hash is: ')
print(old)

# Checks the new hash with the one previously stored
if old == new:
    print("No changes detected")
else:
    print("Changes detected")