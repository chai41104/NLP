import requests
import json

r = requests.get('https://google.com')
print(r.content)