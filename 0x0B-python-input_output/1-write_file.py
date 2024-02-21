#!/usr/bin/python3
"""Definition of file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
