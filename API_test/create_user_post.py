import requests

payload = {
    "name": "Raa_1",
    "job": "automation"
     }
resp = requests.post('https://reqres.in/api/users', data=payload)

print(resp.status_code)
print(resp.json())