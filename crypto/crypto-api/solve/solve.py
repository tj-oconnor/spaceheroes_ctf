import requests


URL = "http://localhost:5000/seq/4fabd002-a494-41fe-93af-c205f12c843b"

r = requests.get
i = 0
while i < 15000 :
    r = requests.get(URL).text
    print(r,end='')
    i +=1
print()


