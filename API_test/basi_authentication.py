import requests

resp = requests.get('https://the-internet.herokuapp.com/basic_auth', auth=("rama", "devi")) # invalid get 401 unautherized

print(resp.status_code)

resp = requests.get('https://the-internet.herokuapp.com/basic_auth', auth=("admin", "admin"))#valid credentials


print(resp.status_code)