#!/usr/bin/python3
'''a Python script requests'''


import requests
import sys

if __name__ == "__main__":

    if not sys.argv[1]:
        payload = {'q': ""}
    else:
        payload = {'q': 'letter'}
    req = requests.post('http://0.0.0.0:5000/search_user', params=payload)

    try:
        res = req.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
