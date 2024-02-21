#!/usr/bin/python3
"""Definition of a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON of the object."""
    return json.dumps(my_obj)
