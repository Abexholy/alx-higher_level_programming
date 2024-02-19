#!/usr/bin/python3
"""Defines a class Function"""


def is_same_class(obj, a_class):
    """Ensure same class and obj is a type of a_class

    Args:
        obj: object to be checked on
        a_class: class type to match

    Returns:
        True if type of obj is a_class
        False, otherwise.
    """
    return type(obj) is a_class
