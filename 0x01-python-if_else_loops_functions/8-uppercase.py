#!/usr/bin/python3
def uppercase(str):
    for intexer in str:
        temp = intexer
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(intexer) - 32)
        print("{}".format(temp), end='')
        print()
