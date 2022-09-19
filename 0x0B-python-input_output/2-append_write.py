#!/usr/bin/python3
""" 2-append_write Module """


def append_write(filename="", text=""):
    """
    Function that writes a string to the end of a
    text file and returns the number of characters.
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
