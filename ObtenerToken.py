print("Esto es solo una DEMO")

import requests
import json

url = "https://10.10.20.14/api/aaaLogin.json"
data = {
    "aaaUser" : {
        "attributes" : {
            "name" : "admin",
            "pwd" : "C1sco12345"
        }
    }
}
cabecera = {"Content-Type" : "application/json"}
respuesta = requests.post(url, json.dumps(data), headers=cabecera, verify=False)
respuesta_json = respuesta.json()

print(respuesta_json)
print("#"*70)
API_Token = respuesta_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
print("API-Token : " + API_Token)

print("#"*70)

