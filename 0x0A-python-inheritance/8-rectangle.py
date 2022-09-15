#!/usr/bin/python3
""" 7-base_geometry Module """


class BaseGeometry():
    """ BaseGeometry class """
    def area(self):
        """ raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ Rectangle class that extends BaseGeometry """
    def __init__(self, width, height):
        """ initializer for Rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
