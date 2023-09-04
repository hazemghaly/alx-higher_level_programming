#!/usr/bin/python3
"""
    define matrix mul
"""


def matrix_mul(m_a, m_b):
    """
        define mul
        raise type error
        Returns a new matrix
    """
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if not all(len(arow) == len(m_a[0]) for arow in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(brow) == len(m_b[0]) for brow in m_b):
        raise TypeError("each row of m_b must should be of the same size")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for roow in m_a for num in roow]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(ro, list) for ro in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all((isinstance(elem, int) or isinstance(elem, float))
               for elem in [num for roww in m_b for num in roww]):
        raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    res = [[0 for x in range(len(m_b))] for y in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for z in range(len(m_b)):
                res[i][j] += m_a[i][z] * m_b[z][j]
    return (res)
