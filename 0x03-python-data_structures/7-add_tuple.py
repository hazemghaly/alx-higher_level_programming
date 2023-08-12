#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = []
    if len(tuple_a) == len(tuple_b):
        for i in range(0, len(tuple_a)):
            a.append(tuple_a[i]+tuple_b[i])
    if len(tuple_b) < 2 and len(tuple_a) == 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
        for i in range(0, len(tuple_a)):
            a.append(tuple_a[i]+tuple_b[i])
    return (tuple(a))
