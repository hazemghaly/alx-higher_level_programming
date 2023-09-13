#!/usr/bin/python3
"""define function ra list of lists of integers representing """


def pascal_triangle(n):
    """difine class that inherits from list:"""
    list = []
    if n <= 0:
        return (list)
    for i in range(n):
        print(','.join(map(str, str(11 ** i))))
