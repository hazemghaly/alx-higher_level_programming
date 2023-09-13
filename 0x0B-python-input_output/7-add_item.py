#!/usr/bin/python3
"""define function named add from_json_string """


import sys

save_to_json_file = __import__('b').save_to_json_file
load_from_json_file = __import__('b').load_from_json_file
try:
    object = load_from_json_file("add_item.json")
except Exception:
    object = []
object.extend(list(sys.argv[1:]))
save_to_json_file(object, "add_item.json")
