#!/usr/bin/python3
"""define function return of available attributes and methods"""


class MyList(list):
    """difine class that inherits from list:"""
    def print_sorted(self):
        """define function print sorted list"""
        print(sorted(self))
