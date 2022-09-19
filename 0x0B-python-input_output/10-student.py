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
        if not attrs:
            return dict

        for item in attrs:
            if type(item) != str:
                return dict

        studentInfo = {}
        for item in attrs:
            try:
                studentInfo[item] = dict[item]
            except:
                Exception
        return studentInfo
