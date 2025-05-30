#!/usr/bin/python3
"""this is our Rectangle class that inherits BaseGeometry
and will be used to make a rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """here is the starting point of our Rectangle
    class that inherits BaseGeometry."""

    def __init__(self, width, height):
        """this init functions initializes the Rectangle
        with the private attributes width and height.
        their values validated using integer_validator function.

        Raises:
            TypeError: if width or height are not integers.
            ValueError: if width or height are <= 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area function will return the height * width"""
        return self.__width * self.__height

    def __str__(self):
        """basic str method that will return
        how a variable of rectangle should be printed like:
        [Rectangle] <width>/<height>"""
        return f"[Rectangle] {self.__width}/{self.__height}"
