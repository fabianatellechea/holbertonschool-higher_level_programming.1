#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = (len(sentence), sentence[0])
    if sentence == '\0':
        tuple = (len(sentence), None)
    return tuple
