#!/usr/bin/python3
"""
Module: json_parser

This module provides a function to convert a JSON string into a
corresponding Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): A string containing a JSON-formatted object.

    Returns:
        any: The Python object decoded from the JSON string.

    Raises:
        json.JSONDecodeError: If the string is not valid JSON.
        TypeError: If the input is not a string.
        Exception: For other unexpected decoding errors.
    """
    return json.loads(my_str)
