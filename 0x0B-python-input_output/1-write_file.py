#!/usr/bin/python3
""" 1-write_file Module """


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file
    and returns the number of characters written.
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
