import requests, json
URL = 'http://127.0.0.1:8000/drfapi2/show_info/'



rq = requests.delete(url=URL + '3/')

print(rq.status_code)  
print(rq.json())