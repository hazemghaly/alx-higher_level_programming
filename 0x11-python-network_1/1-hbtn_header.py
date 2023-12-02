#!/usr/bin/python3
'''a Python script for header'''


import urllib.request
import sys

r = urllib.request.urlopen(sys.argv[1])
print(r.headers['X-Request-Id'])
