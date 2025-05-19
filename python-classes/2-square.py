#!/usr/bin/python3
"""This module is based on 1-square.py which will create a square

the size of square is taken from size and stored privatly also it will be value and type checked
"""


class Square:
    """ Represents square with private size attribute."""
    def __init__(self, size=0):
        """we will initialize size in this method with optional size = 0

        Args:
            size: this will be the size of the square. Must be an integer >= 0.

        Raises:
            TypeError: if size type is not integer.
            ValueError: if size value is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
