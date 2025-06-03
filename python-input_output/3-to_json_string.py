#!/usr/bin/python3
"""
Module: json_converter

This module provides a function to convert a Python object to its
JSON string representation.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of a Python object.

    Args:
        my_obj (any): The Python object to serialize.

    Returns:
        str: The JSON string representation of the object.

    Raises:
        TypeError: If the object is not serializable.
        Exception: For other unexpected errors during conversion.
    """
    return json.dumps(my_obj)
