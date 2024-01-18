import requests


#If we wont get the response with in the mentioned timeout time API will fail

resp = requests.get("https://httpbin.org/delay/10", timeout=5)


print(resp.status_code)