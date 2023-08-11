#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    n = len(sys.argv) - 1
    if n == 0:
        print("{} argument.".format(n))
    elif n > 0:
        print("{} arguments:".format(n))
    for s in range(n):
        print("{}: {}".format(s + 1, sys.argv[s + 1]))
