#!/usr/bin/python3
'''a Python script that fetches'''


import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    htm = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(htm)))
    print("\t- content: {}".format(htm))
    print("\t- utf8 content: {}".format(htm.decode("utf-8")))
