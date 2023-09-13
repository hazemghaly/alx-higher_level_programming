#!/usr/bin/python3
"""define function named from_json_string """


import json


def save_to_json_file(my_obj, filename):
    """define return from_json_string """
    with open(filename, 'w', encoding="utf-8") as f:
        return (json.dump(my_obj, f))
