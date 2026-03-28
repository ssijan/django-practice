import requests, json
URL = 'http://127.0.0.1:8000/drfapi2/show_info/'

data = {
    'course_name':'Bangla',
    'seat':50
}

rq = requests.patch(url = URL + "1/", json=data)

print(rq.status_code)  
print(rq.json())