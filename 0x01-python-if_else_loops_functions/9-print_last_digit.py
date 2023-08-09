#!/usr/bin/python3
def print_last_digit(number):
    ptr = str(number)
    print(int(ptr[-1]), end="")
    return (abs(number) % 10)
