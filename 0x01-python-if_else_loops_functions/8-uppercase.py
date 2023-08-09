#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if s in map(chr, range(ord('a'), ord('z') + 1)):
            s = chr(ord(s) - 32)
        else: s >= 'A' and s <= 'Z' or s == " " or ord(s) in range(49, 58)
        print("{}".format(s), end="")
    print("")
