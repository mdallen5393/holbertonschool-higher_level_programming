#!/usr/bin/python3
""" 2-matrix_divided Module """


def matrix_divided(matrix, div):
    """ Function that performs matrix division
        on a list of lists of integers/floats.
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    temp = len(matrix[0])
    for row in matrix:
        if len(row) != temp:
            raise TypeError("Each row of the matrix must have the same size")

        for entry in row:
            if type(entry) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    newMatrix = []

    for i in range(len(matrix)):
        newMatrix.append([])
        for j in range(len(matrix[i])):
            newMatrix[i].append(round(matrix[i][j] / div, 2))

    return (newMatrix)
