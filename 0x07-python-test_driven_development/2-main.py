#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# matrix = [
#     [1.1375, 2.2, 3.3],
#     [4.4, 5.5, 6.6]
# ]
# matrix = [
#     [1, 3],
#     [5, 7]
# ]
print(matrix_divided(matrix, .3125))
# print(matrix_divided(matrix, 3))
print(matrix)
