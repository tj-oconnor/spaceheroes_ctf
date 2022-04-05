import requests
import re
import base64
import sys


URL = sys.argv[1]

#follow redirect
r = requests.get(URL)
newurl = r.url

print(newurl, flush=True)
i = 0
bin = []
while '~' != (x := requests.get(newurl).text):
    bin.append(x)


"Convert bits to "
b = '01111110'
b64 = ''
for i in range(len(bin)):
    if i % 7 == 0:

        b64 += chr(int(b, 2))
        b = '0'
    b += bin[i]
#Convert string to base64 and get flag
b64 = b64[1:]
missing_padding = len(b64) % 4
if missing_padding:
    b64 += '='* (4 - missing_padding)
print(base64.b64decode(b64),flush=True)
