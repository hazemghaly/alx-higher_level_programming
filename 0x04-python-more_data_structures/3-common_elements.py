#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_set = list(set(set_1))
    my_set2 = list(set(set_2))
    for i in range(len(my_set)):
        if my_set[i] in my_set2:
            return (list(str(my_set[i])))
