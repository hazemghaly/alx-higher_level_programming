#!/usr/bin/python3
"""
    define text
"""


def text_indentation(text):
    """
        define text
        raise type error
        print newline
    """
    i = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while i < len(text):
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print(text[i], end="")
                print("\n")
                i += 1
            if text[i] == " ":
                i += 1
        print(text[i], end="")
        i += 1
