#!/usr/bin/python3
'''a Python script requests'''


import requests
import sys

if __name__ == "__main__":

    w = {'q': ''}
    req = requests.post('http://0.0.0.0:5000/search_user', params = w)
    res = req.json()
    print(f"[{res['id']}] {res['name']}")
