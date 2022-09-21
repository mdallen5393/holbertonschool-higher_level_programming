#!/usr/bin/python3
"""square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializer for Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string representation of Rectangle"""
        return '[' + type(self).__name__ + '] (' + str(self.id) \
            + ') ' + str(self.x) + '/' + str(self.y) + ' - ' \
            + str(self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "size":
                self.size = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for __size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
