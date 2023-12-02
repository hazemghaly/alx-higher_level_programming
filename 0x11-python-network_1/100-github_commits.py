#!/usr/bin/python3
'''listcommits'''
import requests
import sys

if __name__ == "__main__":

    url = 'https://api.github.com/repos/{}/{}/commits/'.format(
        sys.argv[2], sys.argv[1])
    commits = requests.get(url).json()
    try:
        for commit in commits[:10]:
            sha = commits.get("sha")
            author_name = commits.get("commit", {}).get(
                "author", {}).get("name", "Unknown")
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
