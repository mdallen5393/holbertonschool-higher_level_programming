#!/usr/bin/python3


def print_last_digit(number):
    number = str(number)
    last = number[len(number) - 1]
    print(last, end='')
    return (last)
