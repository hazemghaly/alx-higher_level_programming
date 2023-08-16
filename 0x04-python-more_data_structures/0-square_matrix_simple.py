#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    r = len(matrix)
    c = len(matrix[0])
    cpy_max = list(map(list, matrix))
    max = []
    sq = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            max.append(cpy_max[i][j] ** 2)
    sq = [[max[(c) * x + y] for y in range(c)] for x in range(r)]
    return (sq)
