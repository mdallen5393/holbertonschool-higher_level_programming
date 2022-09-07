#!/usr/bin/python3
"""This is the square class!"""


class Square:
    """This class defines a square"""
    def __init__(self, size=None):
        """This initializes a square with a size"""
        try:
            int(size)
            pass
        except TypeError:
            print("size must be an integer")
        try:
            size < 0
            pass
        except ValueError:
            print("size must be >= 0")
        self.__size = size
