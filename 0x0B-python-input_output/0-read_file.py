#!/usr/bin/python3
"""Definition of text file-reading for function."""


def read_file(filename=""):
    """Print the UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
