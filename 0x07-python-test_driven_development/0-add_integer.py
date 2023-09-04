#!/usr/bin/python3
"""
    define add int
    raise type error
    return int
"""

def add_integer(a, b=98):
    """
    define add function
    """
    if isinstance(b, float):
        b = int(b)
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    elif not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    return (int(a + b))
