#!/usr/bin/python3
import random
number = random.randit(-10000, 10000)
last digit = abs(number) % 10
if number < 0:
    digit = -last digit
    print("Last digit of {number:d} is {last_digit:d} and is".format(number, digit), end="")
    if last_digit > 5:
        print("greater than 5")
    elif last_digit == 0:
        print("0")
    else:
        print("less than 6 and not 0")
