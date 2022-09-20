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
                self.height = args[1]
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "size":
                self.width = value
                self.height = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value
