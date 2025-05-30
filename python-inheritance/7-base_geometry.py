#!/usr/bin/python3
"""BaseGeometry class that has unimplemented area function"""


class BaseGeometry():
    """A class with area() function that raises an exception
    because it not implemented yet"""

    def area(self):
        """Empty area method.

        Raises:
            Exception: because area function is not implemented yet.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
