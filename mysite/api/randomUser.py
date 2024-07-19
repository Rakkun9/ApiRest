import requests

api = requests.get('https://randomuser.me/api/')
print(api.status_code)

gender = api.json()['results'][0]['location']['street']['number']
print(gender)

email = api.json()['results'][0]['email']
print(email)