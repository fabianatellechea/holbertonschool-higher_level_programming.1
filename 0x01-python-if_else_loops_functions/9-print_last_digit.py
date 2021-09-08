#!/usr/bin/python3
def print_last_digit(number):
    lnumber = abs(number) % 10
    print("{:d}".format(lnumber), end="")
    return lnumber
