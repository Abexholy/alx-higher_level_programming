#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as j:
        sys.stderr.write("Exception: {}\n".format(j))
        return (False)
    else:
        return (True)
