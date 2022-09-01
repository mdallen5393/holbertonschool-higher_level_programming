#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if not idx < 0 and not idx >= len(my_list):
        for element in my_list:
            new_list.append(element)
        new_list[idx] = element
    return new_list
