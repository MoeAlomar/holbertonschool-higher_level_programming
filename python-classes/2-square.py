#!/usr/bin/python3
"""This module is based on 1-square.py"""


class Square:
    def __init__(self, size=0):
        """we will initialize size in this method

        Args:
            size: this will be the size of the square (type must be an integer or a TypeError will be raised / value must be >= 0 or a ValueError will be raised)

        """
        if size < 0:
            raise ValueError("Size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("Size must be an integer")
        self.__size = size
