#!/usr/bin/python3
'''listcommits'''
import requests
import sys

if __name__ == "__main__":

    url = 'https://api.github.com/repos/{}/{}/commits/'.format(
        sys.argv[2], sys.argv[1])
    commits = requests.get(url).json()
    try:
        for i in commits[:10]:
            print("{}: {}".format(
                commits.get("sha"),
                commits.get("commit").get("author").get("name")))
    except IndexError:
        pass
