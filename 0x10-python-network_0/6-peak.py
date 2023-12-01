#!/usr/bin/python3
""" find_peak """


def find_peak(list_of_integers):
    '''function'''
    start = 0
    end = len(list_of_integers) - 1
    while start < end:
        mid = (start + end) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
    if start == len(list_of_integers) - 1:
        return list_of_integers[start]
    return list_of_integers[start]
