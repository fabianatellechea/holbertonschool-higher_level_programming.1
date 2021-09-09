#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        print("{}".format(str[c] if ord(str[c]) < 97 or ord(str[c]) >
              123 else chr(ord(str[c]) - 32)), end='')
    print()
