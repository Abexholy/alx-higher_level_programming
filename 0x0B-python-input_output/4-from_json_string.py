#!/usr/bin/python3
"""Definition of JSON-to-object function."""
import json


def from_json_string(my_str):
    """Returns the representation of a JSON string."""
    return json.loads(my_str)
