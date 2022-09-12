#!/usr/bin/python3
""" 0-add_integer Module """


def add_integer(a, b=98):
    """ Addition Function for Integers """
    if a is None:
        raise TypeError("'NoneType' object is not subscriptable")
    if a is None:
        raise TypeError("'NoneType' object is not subscriptable")
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
