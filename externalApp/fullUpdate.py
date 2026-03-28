import requests, json
URL = 'http://127.0.0.1:8000/drfapi2/show_info/'

data = {
    'teacher_name':'Adury',
    'course_name':'Bangla',
    'city':'Monohardi',
    'duration': 3,
    'seat':50
}

rq = requests.put(url = URL + "1/", json=data)

print(rq.status_code)  
print(rq.json())