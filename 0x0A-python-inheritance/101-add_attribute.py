#!/usr/bin/python3
"""define function named add_attribute """


def add_attribute(object, a, b):
    """define return add attributes """
    if not object:
        raise TypeError("can't add new attribute")
    return (setattr(object, a, b))
