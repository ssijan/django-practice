import requests, json

URL = 'http://127.0.0.1:8000/drfapi2/show_info/'

data = {
    'teacher_name': 'Adury',
    'course_name': 'English',
    'city': 'Uttora',
    'duration': 3,
    'seat': 4,
}

res = requests.post(URL, json=data)
print(res.status_code)
print(res.json())