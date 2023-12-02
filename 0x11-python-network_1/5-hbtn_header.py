#!/usr/bin/python3
'''a Python script for header requests'''


import requests
import sys

if __name__ == "__main__":

    req = requests.get(sys.argv[1])
    print(dict(req.headers).get("X-Request-Id"))
