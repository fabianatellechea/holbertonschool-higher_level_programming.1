#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lnumber = abs(number) % 10
if number < 0:
    lnumber = -lnumber
print("Last digit of {:d} is {:d}".format(number, lnumber), end=" ")

if lnumber > 5:
    print("and is greater than 5")
elif lnumber == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
