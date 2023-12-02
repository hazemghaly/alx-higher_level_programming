<<<<<<< HEAD
#!/usr/bin/python3
'''a Python script for header'''


import urllib.request
import sys

if __name__ == "__main__":

    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
=======
#!/usr/bin/python3
'''a Python script for header'''


import urllib.request
import sys

# if __name__ == "__main__":
req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    print(dict(response.headers).get("X-Request-Id"))
>>>>>>> 61e3e1bc1485b6e3cc9f3dc882cdd5d400c589fa
