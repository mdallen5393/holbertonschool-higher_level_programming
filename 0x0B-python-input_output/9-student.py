#!/usr/bin/python3
"""9-student Module"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Initializer method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of
        a Student instance
        """
        return vars(self)
