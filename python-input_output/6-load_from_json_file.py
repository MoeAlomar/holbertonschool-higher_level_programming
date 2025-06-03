#!/usr/bin/python3
"""
Module: json_file_loader

This module provides a function to load a Python object from a file
containing JSON data.
"""

import json


def load_from_json_file(filename):
    """
    Loads and returns a Python object from a JSON-formatted file.

    Args:
        filename (str): The path to the JSON file to read from.

    Returns:
        any: The Python object decoded from the JSON content.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
        Exception: For any other errors encountered during reading or
        decoding.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
