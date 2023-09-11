#!/usr/bin/python3
"""define function return of available attributes and methods"""


def is_same_class(obj, a_class):
    """ function returns type an instance of the specified class"""
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
