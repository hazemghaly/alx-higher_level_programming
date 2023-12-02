#!/usr/bin/python3
'''a Python script requests'''


import requests
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    token = sys.argv[2]
    login = requests.get(
        'https://api.github.com/user',
        auth=(username, token))
    res = login.json()
    print("{}".format(res.get("id")))
