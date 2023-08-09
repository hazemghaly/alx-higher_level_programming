#!/usr/bin/python3
ch = map(chr, range(ord('a'), ord('d') + 1))
for alph in ch:
    print(alph.format(ch), end="")
ch = map(chr, range(ord('f'), ord('p') + 1))
for alph in ch:
    print(alph.format(ch), end="")
ch = map(chr, range(ord('r'), ord('z') + 1))
for alph in ch:
    print(alph.format(ch), end="")
