#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as stderr:
        print("Exception: {}".format(stderr))
        return (None)
    return (res)
