import requests  # библиотека для работы с запросами
myServer = 'http://172.21.13.66:8085'  # URL
myMethod = '/tariffoptions/filllinksforcashback'  # URN
# URI = URL + URN
myParam = {'reqid': 1}

myRequest = requests.get(myServer + myMethod, params=myParam)
print(f'URL: {myRequest.url}\nCode: {myRequest.status_code}\nRaw: {myRequest.__dict__}')