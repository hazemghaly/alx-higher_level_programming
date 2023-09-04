#!/usr/bin/python3
"""
    define size
    raise type error
    print #
"""


def print_square(size):
    """
    define size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        if size < 0:
            raise TypeError("size must be an integer")
    if size == 0:
        print("")
    for i in range(0, size):
        for j in range(size):
            print("#", end="")
        print("")
