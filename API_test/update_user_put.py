#PUT -- all the properties of the object should be provided while making the put request

#record exists -- it will update/replace
#recoed doesn't exists ---- will create the record

import requests

payload = {
    "name": "API",
    "job": "zion resident"
      }

resp = requests.put("https://reqres.in/api/users/2", data=payload)

print(resp.json())
print(resp.status_code)