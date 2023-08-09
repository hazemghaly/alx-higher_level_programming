#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if s in map(chr, range(ord('a'), ord('z') + 1)):
            s = chr(ord(s) - 32)
            print("{}".format(s), end="")
    print("")
