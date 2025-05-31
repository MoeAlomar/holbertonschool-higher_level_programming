#!/usr/bin/python3
"""Duck typing exercise with abstract base classes.

This module demonstrates duck typing by creating an abstract class
and implementing it through different classes with the same methods.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class that defines the interface for shapes.

    All concrete shape classes must implement area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """A circle shape that implements the Shape interface."""

    def __init__(self, radius):
        """Initialize a circle with the given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self._radius = radius

    def area(self):
        """Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self._radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self._radius


class Rectangle(Shape):
    """A rectangle shape that implements the Shape interface."""

    def __init__(self, width, height):
        """Initialize a rectangle with the given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self._width = width
        self._height = height

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            float: The area of the rectangle (width * height).
        """
        return self._width * self._height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self._width + self._height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing.

    This function demonstrates duck typing by accepting any object
    that implements the area() and perimeter() methods, without
    explicitly checking its type.

    Args:
        shape: Any object that implements area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
