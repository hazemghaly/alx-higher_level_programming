#!/usr/bin/python3
'''a Python script that fetches with requests'''


import requests

req = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(req.text)))
print("\t- content: {}".format(req.text))
