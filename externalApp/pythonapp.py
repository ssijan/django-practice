import requests 

URL = 'http://127.0.0.1:8000/drfapi2/show_info/'

response = requests.get(url=URL)
print(response.status_code)
# print(type(response))
data = response.json()

print(data)