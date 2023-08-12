#!/usr/bin/python3
def no_c(my_string):
    list_string = list(my_string)
    _string = list_string.copy()
    p = ""
    if 'c' in list_string:
        _string.remove('c')
    if 'C' in list_string:
        _string.remove('C')
    for i in range(len(_string)):
        p += "{}".format(*_string[i])
    return (p)
