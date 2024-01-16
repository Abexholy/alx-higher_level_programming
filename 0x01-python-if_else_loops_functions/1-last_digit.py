#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnumber = abs(number) % 10
if number < 0:
    lastnumber = -(lastnumber)
if lastnumber > 5:
    print(f"Last digit of {number} is {lastnumber} and is greater than 5")
if lastnumber == 0:
    print(f"Last digit of {number} is {lastnumber} and is 0")
elif lastnumber < 6:
    print(f"Last digit of {number} is {lastnumber} and is less than 6 and not 0")
