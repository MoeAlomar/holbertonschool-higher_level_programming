#!/usr/bin/python3
"""Defines the Square class.

This module provides a class to represent a square,
with basic size validation.
"""


class Square:
    """Represents a square with size validation.

    This class defines a square and validates that the size is an integer
    greater than or equal to zero. The size is stored as a private attribute.
    """
    def __init__(self, size=0):
        """Initializes a Square instance.

        Args:
            size (int, optional): The size (length of a side) of the square.
            Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
