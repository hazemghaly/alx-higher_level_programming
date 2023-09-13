#!/usr/bin/python3
"""define function named from_json_string """


import json


def load_from_json_file(filename):
    """define return from_json_string """
    with open(filename, 'r') as f:
        return (json.load(f))
