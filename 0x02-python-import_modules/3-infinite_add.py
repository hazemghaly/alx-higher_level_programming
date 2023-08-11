#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    n = len(sys.argv) - 1
    x = 0
    for s in range(1, n + 1):
        if sys.argv[s].isnumeric():
            if int(sys.argv[s]) < 0:
                x = int(sys.argv[s])
        x += int(sys.argv[s])
    print("{}".format(x))
