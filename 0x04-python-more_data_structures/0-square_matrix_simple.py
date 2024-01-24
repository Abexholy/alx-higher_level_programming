#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    abex_matrix = matrix.copy()

    for j in range(len(matrix)):
        abex_matrix[j] = list(map(lambda x: x**2, matrix[j]))

    return (abex_matrix)
