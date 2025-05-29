#!/usr/bin/python3
"""this module extends rectangle to make a square, because every square
is a rectangle but vice bersa is not always right."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square uses init to initialize a square with a specefic size.
    with the private attr: size."""

    def __init__(self, size):
        """in this initializer we will initialize a square with
        the specified size after checking for its validation
        using integer validator function.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is equal or less than 0."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """in this function were calculating the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """String representation clearifies that it is a square
        and its height and width."""
        return f"[Square] {self.__size}/{self.__size}"
