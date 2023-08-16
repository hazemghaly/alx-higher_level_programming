#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cpy_max = list(map(list, matrix))
    max = []
    sq = []
    for i in range(len(cpy_max)):
        for j in range(len(cpy_max)):
            max.append(cpy_max[i][j] ** 2)
    sq = [[max[(j + 1) * x + y] for y in range(j + 1)] for x in range(i + 1)]
    return (sq)
