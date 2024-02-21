#!/usr/bin/python3
"""Definition of text file function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line of strings in file.

    Args:
        filename : The name of file.
        search_string : The string to search for within all file.
        new_string : The string to be inserted.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
