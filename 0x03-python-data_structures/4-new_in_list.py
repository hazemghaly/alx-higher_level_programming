#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return (my_list)
    cpy_list = []
    for s in range(len(my_list)):
        cpy_list.append(my_list[s])
    cpy_list[idx] = element
    return (cpy_list)
