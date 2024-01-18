import requests
#we can pass params to the get meethod
parms = {"page": 2}
#resp = requests.get('https://reqres.in/api/users?page=2')
resp = requests.get('https://reqres.in/api/users', params=parms)

print(resp)
print(dir(resp)) ###to get the list methods this resp variable has


code = resp.status_code
assert code == 200, "Code does not match"

#print(resp.text) #return data in unicode
#print(resp.content) # return data in bytes
print(resp.json()) #return data in json formate

print(resp.headers)
print(resp.cookies)
print(resp.encoding)
print(resp.url)

#to view the json data use this link past the json_response output here
json_response = resp.json()
print(json_response['total_pages'])
assert json_response['total_pages'] == 2, "Total pages count doesnot matching"

print(json_response["data"][0]["email"])
assert (json_response["data"][0]["email"]).endswith("reqres.in")
