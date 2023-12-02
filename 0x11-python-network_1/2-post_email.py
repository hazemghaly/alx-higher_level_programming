#!/usr/bin/python3
'''a Python script for post mail'''


import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    e = urllib.parse.urlencode({'email': sys.argv[2]})
    data = e.encode('utf-8')

    req = urllib.request.Request(
        sys.argv[1], data, method="POST")
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
