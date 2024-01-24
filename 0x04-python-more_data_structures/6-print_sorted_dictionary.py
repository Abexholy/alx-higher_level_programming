#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    abex_ord = list(a_dictionary.keys())
    abex_ord.sort()
    for j in abex_ord:
        print("{}: {}".format(j, a_dictionary.get(j)))
