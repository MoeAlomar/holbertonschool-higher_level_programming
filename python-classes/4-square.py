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

    @property
    def size(self):
        """Getter method of size instance

        Returns:
            int: size of square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Defined area method in class square

        Returns:
            (int): area of the square be returning self.__size * self.__size.
        """
        return self.__size ** 2
