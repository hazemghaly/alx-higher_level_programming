#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = []
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) == 3 or len(tuple_a) == 3:
        for i in range(len(tuple_a) - 1):
            a.append(tuple_a[i]+tuple_b[i])
    else:
        for i in range(len(tuple_a)):
            a.append(tuple_a[i]+tuple_b[i])
    return (tuple(a))
