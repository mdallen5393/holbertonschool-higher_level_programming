#!/usr/bin/python3
""" 7-base_geometry Module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that extends Rectangle """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """ prints square dimensions """
        return("[Rectangle] {}/{}".format(self.__size, self.__size))
