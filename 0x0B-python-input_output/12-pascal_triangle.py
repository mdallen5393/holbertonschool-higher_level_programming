#!/usr/bin/python3
"""12-pascal_triangle Module"""


def pascal_triangle(n):
    """
    Function that returns a list of lists containing
    Pascal's Triangle.
    """
    if n <= 0:
        return []

    pascal = []

    for i in range(n):
        row = []
        row.append(1)
        for j in range(2, i + 1):
            row.append(0)
        pascal.append(row)

    prev = pascal[0]
    for i in range(1, n):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        pascal[i].append(1)
    return pascal
