#!/usr/bin/python3
"""Defines a list class MyList"""


class MyList(list):
    """ Class that inherits attributes references of class list

    Args:
        list: The class list
    """

    def print_sorted(self):
        """This are Method that prints the sorted list in order"""
        print(sorted(self))
