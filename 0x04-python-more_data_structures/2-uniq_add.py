#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    my_set = list(set(my_list))
    for i in range(len(my_set)):
        a = my_set[i] + a 
    return (a)
