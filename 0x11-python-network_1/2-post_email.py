#!/usr/bin/python3
'''a Python script for post mail'''


import urllib.request
import sys

if __name__ == "__main__":
    email = sys.argv[2]

    req = urllib.request.Request(
        sys.argv[1], email.encode('utf-8'), method="POST")
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
