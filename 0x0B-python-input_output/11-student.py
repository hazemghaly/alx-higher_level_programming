#!/usr/bin/python3
"""define function return of available attributes and methods"""


class Student:
    """difine class that inherits from list:"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary represntation"""

        try:
            for a in attrs:
                if type(a) is not str:
                    return (self.__dict__)
        except Exception:
            return (self.__dict__)

        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            h_dict = dict()
            for k, vlu in self.__dict__.items():
                if k in attrs:
                    h_dict[k] = vlu
            return (h_dict)

    def reload_from_json(self, json):
        """replace"""
        for kk, vlue in json.items():
            if kk in self.__dict__:
                self.__dict__[kk] = vlue
