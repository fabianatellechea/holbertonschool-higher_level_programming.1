#!/usr/bin/python3
def uppercase(str):
    d = ord("a") - ord("A")
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            c = ord(c) - d
            print("{}".format(chr(c)), end="")
        else:
            print("{}".format(c), end="")
    print()
