#!/usr/bin/python3
"""10-student Module"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Initializer method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of
        a Student instance
        """
        dict = vars(self)
        if attrs is None:
            return dict

        studentInfo = {}
        for item in attrs:
            if item in dict:
                studentInfo[item] = dict[item]
        return studentInfo

    def reload_from_json(self, json):
        """
        Function that replaces all attributes of the
        Student instance.
        """
        self.__dict__.update(json)
