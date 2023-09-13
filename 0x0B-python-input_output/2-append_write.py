#!/usr/bin/python3
"""define function named write_file """


def append_write(filename="", text=""):
    """define return write_file """

    with open(filename, 'a', encoding="utf-8") as file:
        return (file.write(text))
