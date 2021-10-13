#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string and returns the number of characters added"""
    with open(filename, 'a') as f:
        return f.write(text)
