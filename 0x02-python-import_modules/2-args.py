#!/usr/bin/env python3
if __name__ == '__2-args__':
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{} argument.".format(n))
    elif n > 0:
        print("{} arguments:".format(n))
    for s in range(1, n + 1):
        print("{}: {}".format(s, sys.argv[s]))
