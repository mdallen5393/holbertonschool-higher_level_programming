#!/usr/bin/python3
""" 3-say_my_name Module """


def say_my_name(first_name, last_name=""):
    """ Function that prints the input names """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
