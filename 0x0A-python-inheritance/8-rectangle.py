#!/usr/bin/python3
""" 7-base_geometry Module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that extends BaseGeometry """
    def __init__(self, width, height):
        """ initializer for Rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
