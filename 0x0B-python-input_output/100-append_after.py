#!/usr/bin/python3
"""define function ra list of lists of integers representing """


def append_after(filename="", search_string="", new_string=""):
    """difine search:"""
    with open(filename, 'r', encoding="utf-8") as f:
        temp = []
        while (1):
            i = f.readline()
            if i == "":
                break
            temp.append(i)
            if search_string in i:
                temp.append(new_string)
    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(temp)
