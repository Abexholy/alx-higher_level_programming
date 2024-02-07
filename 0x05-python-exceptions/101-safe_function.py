#!/usr/bin/python3
import sys


def safe_function(fct, *args):

    try:
        tanks = fct(*args)
    except Exception as j:
        sys.stderr.write("Exception: {}\n".format(j))
        tanks = None

    return (tanks)
