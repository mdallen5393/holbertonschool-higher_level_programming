#!/usr/bin/python3
"""8-class_to_json Module"""


def class_to_json(obj):
    """
    Function that returns the dictionary description
    with simple data structure (list, dictionary,
    string, integer, and boolean) for JSON serialization
    of an object.
    """
    return vars(obj)
