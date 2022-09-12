#!/usr/bin/python3
""" 4-print_square Module """


def print_square(size):
    """ Function that prints squares using '#' """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
