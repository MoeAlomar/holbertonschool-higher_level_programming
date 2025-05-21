#!/usr/bin/python3
"""Module defining a Square class with size encapsulation.

This module contains a class used to represent a square
by storing the size (length of one side) as a private attribute.
The Square class does not expose the size directly and
does not include additional behavior such as computing area.
"""


class Square:
    """Represents a square.

    This class defines a square by encapsulating its size.
    The size is stored as a private attribute and cannot be accessed directly.
    """
    def __init__(self, size):
        """Initializes a Square instance with a given size.

        Args:
            size (int or float): The size (length of one side) of the square.
        """
        self.__size = size
