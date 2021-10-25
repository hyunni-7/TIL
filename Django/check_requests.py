import requests
from pprint import pprint

response = requests.get('http://127.0.0.1:8000/api/v1/json-3/')
response_json = response.json()

pprint(response_json)
# print(len(response_json))
print('-' * 80)
pprint(response_json[0])
