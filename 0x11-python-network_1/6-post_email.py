#!/usr/bin/python3
'''a Python script for pst email requests'''


import requests
import sys


if __name__ == "__main__":
    a = {'email': sys.argv[2]}

    req = requests.post(sys.argv[1], data = a)
    print(req.text)
