#!/usr/bin/python3
"""
Module: file_appender

This module provides a function to append text to a UTF-8 encoded file.
If the file does not exist, it will be created.
"""


def append_write(filename="", text=""):
    """
    Appends the given text to a UTF-8 encoded text file.

    Args:
        filename (str): The name of the file to append to. Defaults to an
        empty string.

        text (str): The text content to append to the file. Defaults to an
        empty string.

    Returns:
        int: The number of characters written to the file.

    Raises:
        FileNotFoundError: If the file path is invalid.
        UnicodeEncodeError: If the text cannot be encoded in UTF-8.
        Exception: For any other issues encountered while opening or
        writing to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
