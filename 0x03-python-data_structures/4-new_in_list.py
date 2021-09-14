#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    i = len(my_list) - 1
    new_list = list(my_list)

    if idx < 0 or idx > i:
        return my_list
    else:
        new_list[idx] = element
        return new_list
