import requests
import json

data = open("data.json", "r").read()
resp = requests.post('https://reqres.in/api/users', json=json.loads(data))

print(resp.status_code)
print(resp.headers.get("Content-Type"))
print(resp.headers.get("Authentication"))
print(resp.json())