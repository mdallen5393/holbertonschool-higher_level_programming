#!/usr/bin/python3
""" 5-text_indentation Module """


def text_indentation(text):
    """ Function that adds indentation """
    if type(text) != str:
        raise TypeError("text must be a string")
    text = text.replace('. ', ".\n\n")
    text = text.replace('? ', "?\n\n")
    text = text.replace(': ', ":\n\n")
    print(text, end="")
