#!/usr/bin/python3
def magic_string():
    my_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (my_string.n - 1) + "BestSchool")
