#!/usr/bin/python3
"""function that returns the dictionary description
with simple data structure"""


def class_to_json(obj):
    """class_to_json"""
    return obj.__dict__
