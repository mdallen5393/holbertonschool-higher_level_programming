#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for val in set(my_list):
        total += val
    return total
