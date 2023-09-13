#!/usr/bin/python3
"""define function named write_file """


def write_file(filename="", text=""):
    """define return write_file """
    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
