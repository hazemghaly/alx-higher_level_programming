#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        x = str[:n]
        y = str[n+1:]
        return (x + y)
    else:
        return (str)
