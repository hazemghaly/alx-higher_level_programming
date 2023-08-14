#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list) - 1
    cpy_list= my_list[x::-1]
    for i in cpy_list:
        print("{:d}".format(i))
