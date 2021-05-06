import requests

req = requests.get(url='http://numbersapi.com/31/math?json=true')
print(req.json()['found'])