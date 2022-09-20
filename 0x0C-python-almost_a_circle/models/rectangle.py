#!/usr/bin/python3
"""
rectangle module that defines the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer for Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """method to calculate area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """method to display a rectangle using `#`"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """return string representation of Rectangle"""
        return '[Rectangle] (' + str(self.id) + ') ' \
            + str(self.__x) + '/' + str(self.__y) + ' - ' \
            + str(self.__width) + '/' + str(self.__height)

    @property
    def width(self):
        """Getter for __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for __width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for __height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for __x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for __x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for __y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for __y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
