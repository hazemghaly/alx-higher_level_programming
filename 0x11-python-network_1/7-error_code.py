#!/usr/bin/python3
'''a Python script rise error requests'''


import requests
import sys

if __name__ == "__main__":

    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(req.text)
