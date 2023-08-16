#!/usr/bin/python3
def no_c(my_string):
    list_string = list(my_string)
    _string = list_string.copy()
    p = ""
    for i in range(len(list_string)):
        if "c" or "C" in _string:
            if 'c' in _string:
                _string.remove('c')
            if 'C' in _string:
                _string.remove('C')
    for i in range(len(_string)):
        p += "{}".format(*_string[i])
    return (p)
