#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    i = 0
    try:
        while y < x:
            if type(my_list[y]) is int:
                print("{:d}".format(my_list[y]), end='')
                i += 1
            y += 1
    except (ValueError, TypeError):
        return (IndexError)
    print()
    return (i)
