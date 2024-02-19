#!/usr/bin/python3
"""Defines class inherited function"""


def is_kind_of_class(obj, a_class):
    """Function that checks if obj is same as the instance of a_class

    Args:
        obj: object to be checked
        a_class: class type to match obj

    Returns:
        True if obj is an instance of a_class
        False, otherwise
    """
    return isinstance(obj, a_class)
