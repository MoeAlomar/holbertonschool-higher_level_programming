#!/usr/bin/python3
"""This module creates a class named Square

it makes a square with a specified size.
"""


class Square:
    """A class named Square

    Attributes:
    attr1 (size): size of square
    """

    def __init__(self, size=0):
        """Initializes an instance of square

        Args:
        size (int): size for __size attribute of class instance
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
