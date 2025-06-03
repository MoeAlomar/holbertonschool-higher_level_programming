#!/usr/bin/python3
"""
Module: json_file_saver

This module provides a function to save a Python object to a file in
JSON format using UTF-8 encoding.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a file in JSON format.

    Args:
        my_obj (any): The Python object to serialize and write.
        filename (str): The path to the file where the JSON data will be
        stored.

    Raises:
        TypeError: If the object is not serializable.
        FileNotFoundError: If the file path is invalid.
        Exception: For other errors during writing or serialization.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
