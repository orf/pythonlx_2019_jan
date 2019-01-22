import requests
import pprint

response = requests.post('https://httpbin.org/anything', auth=('user', 'password'), json={'a': 'b'})
pprint.pprint(response.json())
print(response.text)
