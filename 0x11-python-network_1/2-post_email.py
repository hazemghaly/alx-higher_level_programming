#!/usr/bin/python3
'''a Python script for post mail'''


import urllib.request
import urllib.request
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode('utf-8')

    req = urllib.request.Request(
        sys.argv[1], data, method="POST")
    with urllib.request.urlopen(req) as response:
        print(f"Your email is: {response.read().decode('utf-8')}")
