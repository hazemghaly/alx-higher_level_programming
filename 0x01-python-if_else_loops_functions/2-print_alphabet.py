#!/usr/bin/python3
ch = map(chr, range(ord('a'), ord('z') + 1))
for alph in ch:
    print(alph.format(ch), end="")
