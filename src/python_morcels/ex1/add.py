import sys


def add(matrix1, matrix2):
    return [
        [sum(tuple) for tuple in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
    ]


matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
print(add(matrix1, matrix2))

matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
print(add(matrix1, matrix2))


def add_multiple(*matrices):
    return [
        [sum(tuple) for tuple in zip(*rows)]
        for rows in zip(*matrices)
    ]


matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]
print(add_multiple(matrix1, matrix2, matrix3))


def shape(matrix):
    return tuple([len(row) for row in matrix])


def add(*matrices):
    s = shape(matrices[0])

    if not all([s == shape(matrix) for matrix in matrices]):
        raise ValueError("Given matrices are not the same size.")

    return [
        [sum(row) for row in zip(*rows)]
        for rows in zip(*matrices)
    ]


matrix1 = [[1, 9], [7]]
matrix2 = [[1, 2], [3, 0]]

print(add(matrix1, matrix2))
