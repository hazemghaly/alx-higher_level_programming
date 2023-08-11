#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    n = len(sys.argv) - 1
    x = 0
    for s in range(1, n + 1):
        x = x + int(sys.argv[s])
    print("{}".format(x))
