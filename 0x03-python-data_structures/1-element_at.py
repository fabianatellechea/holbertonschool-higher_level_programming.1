#!/usr/bin/python3
def element_at(my_list, idx):
    i = len(my_list)
    if idx < 0 or idx > i:
        return None
    else:
        return idx + 1
