#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for row in matrix:
        new_row = []
        square.append(new_row)
        for item in row:
            new_row.append(item ** 2)
    return square
