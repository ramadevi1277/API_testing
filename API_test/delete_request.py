import requests

resp = requests.delete('https://reqres.in/api/users/1000000000000')

#print(resp.status_code)
assert resp.status_code == 204

#we did nit get any response for the delete user