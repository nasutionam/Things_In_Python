import requests
import json

data = {
        'username' : 'tes@tes.com',
        'email' : 'tes@tes.com',
        'password': 'tes',
        'name' : 'tes',
        'phone_number' : '+12312312'
}
r = requests.post('https://sensorwkwkw.wkwk', data=data)

print(r.json())