#!/usr/bin/python3
"""define function return of available attributes and methods"""


def inherits_from(obj, a_class):
    """ function returns type an instance of the specified class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
