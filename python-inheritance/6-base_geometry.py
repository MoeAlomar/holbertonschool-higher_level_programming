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
