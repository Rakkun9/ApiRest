import requests

api = requests.get('https://randomuser.me/api/')
print(api.status_code)

name = api.json()['results'][0]['name']['first']
email = api.json()['results'][0]['email']
gender = api.json()['results'][0]['gender']
password = api.json()['results'][0]['login']['password']
phone = api.json()['results'][0]['phone']
