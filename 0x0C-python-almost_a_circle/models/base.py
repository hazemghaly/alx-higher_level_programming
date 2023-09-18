#!/usr/bin/python3
"""define class named base """


class Base:
    """difine class named a base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
