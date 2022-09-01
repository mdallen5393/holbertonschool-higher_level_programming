#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = None
    if not idx < 0 and not idx >= len(my_list):
        for i in range(len(my_list) - 1):
            new_list[i] = my_list[i]
        new_list[idx] = element
        return new_list
