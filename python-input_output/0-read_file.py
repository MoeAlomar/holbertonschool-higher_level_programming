#!/usr/bin/python3
"""
Module: file_reader

This module provides a function to read the first line from a
UTF-8 encoded file.
"""


def read_file(filename=""):
    """
    Reads and returns the first line of a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to read from. Defaults to
        an empty string.

    Returns:
        str: The first line of the file with trailing newline removed,
        or an empty string if the file is empty or filename is empty.

    Raises:
        FileNotFoundError: If the file does not exist.
        UnicodeDecodeError: If the file cannot be decoded using UTF-8.
        Exception: For any other issues encountered while opening or
        reading the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return f.readline().rstrip('\n')
