import requests

#specify only the property that you want to modify

payload = {
    "name": "devisubbu"
    }
resp = requests.patch('https://reqres.in/api/users/2', data=payload)

print(resp.status_code)