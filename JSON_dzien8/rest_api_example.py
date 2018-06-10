import hashlib
import requests

BASE_URL = 'http://polakow.eu:3000/people/'

response = requests.get(BASE_URL,
                        params={'_limit': 3, 'page': 2})
print(response.json()) #zdekodowany obiekt; u nas wychodzi lista ze zdekowanymi slownikami
print(response.text)
print(response.headers)
print(response.status_code)
print(response.headers['X-Total-Count'])

md5 = hashlib.md5('relayr'.encode('ascii'))
token = md5.hexdigest()
print(token)
headers = {"Authorization": 'Bearer ' + token}
person = {'first_name': "Jaime", 'last_name': 'lannister', 'email': 'hearmeroar@onet.pl', 'phone': '+46786543', 'ip_address': '192.168.1.1'}

response = requests.post(BASE_URL, json=person, headers=headers)
print('ok')
cebularze = requests.get(BASE_URL, params={'last_name': 'Cebularz'}).json()
print(cebularze)

response = requests.get(BASE_URL, params={'email_like': '@gmail.com'}).json() #koncowka like pozwala na wyszukanie rekordow z zadanym fragmentem adresu email
print(response)