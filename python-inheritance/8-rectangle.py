#!/usr/bin/python3
"""this is our Rectangle class that inherits BaseGeometry
and will be used to make a rectangle.
"""


class Rectangle(BaseGeometry):
    """here is the starting point of our Rectangle class that inherits BaseGeometry."""

    def __init__(self, width, height):
        """this init functions initializes the Rectangle
        with the private attributes width and height.
        their values validated using integer_validator function.
        """
        interger_validator(self.__width, width)
        integer_validator(self.__height, height)
