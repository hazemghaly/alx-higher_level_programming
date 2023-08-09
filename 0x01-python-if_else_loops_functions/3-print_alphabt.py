#!/usr/bin/python3
ch = map(chr, range(ord('a'), ord('z') + 1))
for alph in ch:
    if alph not in 'eq':
        print(alph.format(ch), end="")
