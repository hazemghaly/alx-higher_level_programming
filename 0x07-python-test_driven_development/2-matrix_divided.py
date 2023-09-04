#!/usr/bin/python3
"""
    define matrix div
"""


def matrix_divided(matrix, div):
    """
        define div
        raise type error
        Returns a new matrix
    """
    h = len(matrix)
    c = len(matrix[0])
    r = []
    d = []
    di = []
    cpy_max = list(map(list, matrix))
    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        r.append(len(row))
    for g in range(len(r)):
        if not r[0] == r[g]:
            raise TypeError("Each row of the matrix must have the same size")
    m = all(type(f) is list for f in matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int):
                if not isinstance(matrix[i][j], float):
                    if m is not False:
                        raise TypeError("matrix must be a \
matrix (list of lists)\
 of integers/floats")
            d.append(round(cpy_max[i][j] / div, 2))
    di = [[d[(c) * x + y] for y in range(c)] for x in range(h)]
    return (di)
