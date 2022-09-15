#!/usr/bin/python3
""" 0-lookup Module """


def lookup(obj):
    """
    Function that returns the list of available
    attributes and methods of an object
    """
    atts_and_mets = list(dir(obj))
    return atts_and_mets
