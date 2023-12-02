#!/usr/bin/python3
'''a Python script rise error'''


import urllib.request
import sys

if __name__ == "__main__":

    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.URLError as e:
        print(f"Error code: {e}")
