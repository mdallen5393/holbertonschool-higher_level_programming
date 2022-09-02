#!/usr/bin/python3
def multiple_returns(sentence):
    char, strlen = None, len(sentence)
    if strlen > 0:
        char = sentence[0]
    return ((strlen, char))
