#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if not idx < 0 and not idx >= len(my_list):
        my_list[idx] = element
    return my_list
