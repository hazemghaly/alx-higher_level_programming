#!/usr/bin/python3
def weight_average(my_list=[]):
    v, w = 0, 0
    if len(my_list) == 0:
        return (0)
    for x in my_list:
        v += (x[0] * x[1])
        w += x[1]
    return (v / w)
