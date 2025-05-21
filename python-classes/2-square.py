#!/usr/bin/python3
"""This module creates a class named Square

It makes a square with a specified size.
"""


class Square:
    """Represents a square with a validated size.

    The size must be an integer >= 0. It is stored as a private attribute
    initialized by default to 0.
    """
    def __init__(self, size=0):
        """Initializes an instance of square

        Args:
            size (int): size for __size attribute of class instance

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
