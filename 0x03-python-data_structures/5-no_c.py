#!/usr/bin/python3
def no_c(my_string):
    list = ['c', 'C']
    str2 = "".join(i for i in my_string if i not in list)
    print(str2)
