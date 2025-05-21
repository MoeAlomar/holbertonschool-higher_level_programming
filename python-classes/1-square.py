#!/usr/bin/python3
"""This module defines a Square class with a private size attribute.

This module contains a class used to represent a square
by storing the size (length of one side) as a private attribute.
The Square class does not expose the size directly and
does not include additional behavior such as computing area.
"""


class Square:
    """Here in this class we will define __init__ method which will assign the __size value"""

    def __init__(self, size):
        """initializes the square with a given size.

        Args:
            size: the size of the square should be an integer (no type/value validation).
        """
        self.__size = size
