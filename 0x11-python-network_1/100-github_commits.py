#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""
import requests
import sys

if __name__ == "__main__":

    url = ' https://developer.github.com/v3/repos/{}/{}/commits/'.format(
        sys.argv[2], sys.argv[1])
    commits = requests.get(url).json()

    try:
        for commit in commits[:10]:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
