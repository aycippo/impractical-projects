import sys
import random
import requests
from requests.auth import HTTPBasicAuth
import os

uri = 'https://randommer.io/api/Name'
api_key = os.environ['RANDOMMER_API_KEY']
headers = {'x-api-key': api_key}
params = {'nameType': 'fullname', 'quantity': '1'}
get = requests.get(uri, headers=headers, params=params).json()
print(get)
