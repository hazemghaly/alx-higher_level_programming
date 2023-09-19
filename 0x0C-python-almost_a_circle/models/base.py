#!/usr/bin/python3
"""define class named base """


import json


class Base:
    """difine class named a base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """define return to_json_string """
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return (json.dumps(list_dictionaries))

@classmethod
    def save_to_file(cls, list_objs):
        """define return to_json_string """
        filename = str(cls.__name__) + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            dicts = [b.to_dictionary() for b in list_objs]
            file.write(Base.to_json_string(dicts))
