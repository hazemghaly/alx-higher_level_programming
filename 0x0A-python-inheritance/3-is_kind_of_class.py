#!/usr/bin/python3
"""define function return of available attributes and methods"""


def is_kind_of_class(obj, a_class):
    """ function returns type an instance of the specified class"""
    if issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)
