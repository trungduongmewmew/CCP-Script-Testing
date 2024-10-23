import requests
import subprocess
url = "https://cyberark.mylab.local/AIMWebService/api/Accounts"
params = {
    "AppID": "RESTAPI",
    "Safe": "CCP_Testing",
    "Object": "Operating System-MTech-Win-Local-10.10.11.3-administrator"
}
response = requests.get(url, params=params, verify=False)
if response.status_code == 200:
    data = response.json()
    tontent = data['Content']
    tsername = data['UserName'] 
    print(f"UserName: {tsername}")
    print(f"Password: {tontent}")
else:
    print(f"Error: {response.status_code}")
def open_remote_desktop(ip_address, username, password):
    subprocess.run([
        "cmdkey", "/generic:TERMSRV/{ip}".format(ip=ip_address),
        "/user:{user}".format(user=username),
        "/pass:{pwd}".format(pwd=password)
    ])
    subprocess.run(["mstsc", "/v:{}".format(ip_address)])
open_remote_desktop("10.10.11.3", tsername, tontent)
