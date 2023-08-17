#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = {i for i in a_dictionary if a_dictionary[i] == value}
    for j in key:
        if j in a_dictionary.keys():
            a_dictionary.pop(j)
    return (a_dictionary)
