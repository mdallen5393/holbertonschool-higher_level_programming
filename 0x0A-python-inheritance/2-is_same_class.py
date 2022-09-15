#!/usr/bin/python3
""" 2-is_same_class.py Module """


def is_same_class(obj, a_class):
    """
    returns `True` if the object is exactly an
    instance of the specified class
    """
    return type(obj) == a_class
