#!/usr/bin/python3
def search_replace(my_list, search, replace):
    x = []
    for j in range(len(my_list)):
        x.append(my_list[j])
    for i in range(len(my_list)):
        if x[i] == search:
            x[i] = replace
    return (x)
