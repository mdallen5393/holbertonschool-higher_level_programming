#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        for element in my_list:
            if element % 2 == 0:
                element = "True"
            else:
                element = "False"
    return my_list
