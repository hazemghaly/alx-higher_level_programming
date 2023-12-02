#!/usr/bin/python3
'''a Python script rise error requests'''


import requests
import sys

if __name__ == "__main__":

    try:
        req = requests.get(sys.argv[1])
        print(req.text)

    except requests.HTTPError as e:
        print(f"Error code: {e.code}")
