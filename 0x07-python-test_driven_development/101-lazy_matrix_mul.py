#!/usr/bin/python3
"""
    define matrix mul
"""


def lazy_matrix_mul(m_a, m_b):
    """
        define mul
        raise type error
        Returns a new matrix
    """
    import numpy as np


    if len(m_a) == 0:
        raise ValueError("m_a is empty")
    if len(m_b) == 0:
        raise ValueError("m_b is empty")
    if not all(len(arow) == len(m_a[0]) for arow in m_a):
        raise TypeError("each row of m_a not the same size")
    if not all(len(brow) == len(m_b[0]) for brow in m_b):
        raise TypeError("each row of m_b not the same size")
    if not isinstance(m_a, list):
        raise TypeError("m_a not a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b not a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a not a list of lists")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for roow in m_a for num in roow]):
        raise TypeError("m_a should contain only int or floats")
    if not all(isinstance(ro, list) for ro in m_b):
        raise TypeError("m_b not a list of lists")
    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [num for roww in m_b for num in roww]):
        raise TypeError("m_b should contain only int or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiply")
    return (np.dot(m_a,m_b))
