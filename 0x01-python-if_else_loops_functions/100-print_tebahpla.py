#!/usr/bin/python3
for s in range(122, 96, -1):
    if s % 2 == 0:
        print(chr(s), end="")
    else:
        print(chr(s - 32), end="")
