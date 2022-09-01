#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for entry in row:
                print("{:d}".format(entry), end=' ')
            print()
