#!/usr/bin/python3
'''a Python script for pst email requests'''


import requests
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}

    req = requests.post(sys.argv[1], data)
    print(req.text())
