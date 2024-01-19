#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    comma = my_list[:]
    if idx < 0:
        return comma
    if idx > len(my_list) - 1:
        return comma
    comma[idx] = element
    return comma
