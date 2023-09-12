#!/usr/bin/python3
"""define function named add_attribute """


def read_file(filename=""):
    """define return add attributes """
    with open(filename, 'r', encoding="utf-8") as f:
	for line in f:
            print(line.strip())
	f.close()
