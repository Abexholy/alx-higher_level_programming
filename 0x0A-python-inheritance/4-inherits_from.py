#!/usr/bin/python3
"""This defines an inherited function"""



def inherits_from(obj, a_class):
    """Function that checks if obj is same as an instance of a_class

    Args:
        obj: object to be checked
        a_class: class type to obj

    Returns:
        True if obj is an instance of an a_class
        False, otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
