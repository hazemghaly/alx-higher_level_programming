#!/usr/bin/python3
"""define function return of available attributes and methods"""


class Student:
    """difine class that inherits from list:"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary represntation"""
        return (self.__dict__)
