#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_list = []
    for s in range(len(my_list)):
        cpy_list.append(my_list[s])
    if idx >= 0 and idx < len(my_list):  
        cpy_list[idx] = element
        return (cpy_list)
    else:
        return(cpy_list)
