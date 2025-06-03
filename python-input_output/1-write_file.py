#!/usr/bin/python3
"""
Module: file_writer

This module provides a function to write text to a UTF-8 encoded file.
If the file exists, it will be overwritten.
"""


def write_file(filename="", text=""):
    """
    Writes the given text to a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to write to. Defaults to an
        empty string.

        text (str): The text content to write into the file. Defaults to
        an empty string.

    Returns:
        int: The number of characters written to the file.

    Raises:
        FileNotFoundError: If the file path is invalid.
        UnicodeEncodeError: If the text cannot be encoded in UTF-8.
        Exception: For any other issues encountered while opening or
        writing to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
