#!/usr/bin/python3
from abc import ABC, abstractmethod
import math
"""in this module we should try duck typing by creating an abstract class
and implementing it through different classes with the same methods."""


class Shape(ABC):
    """Shape is our abstract class that we will implement
    and all its methods are abstract."""
    @abstractmethod
    def area(self):
        """area is a an abstract method to be implemented."""
        pass

    @abstractmethod
    def perimeter(self):
        """an abstract method to calc the perimeter"""
        pass


class Circle(Shape):
    """Circle is a class that implements the abstract Shape class."""

    def __init__(self, radius):
        """initializer method of circle class
        Args:
            radius: is an integer and refers to the 'radius' of the circle.
        """
        self._radius = radius

    def area(self):
        """here we are implementing the area method for circle class
        to calculate the area of the circle and return it"""
        return math.pi * (self._radius**2)

    def perimeter(self):
        """this method is implemented to calculate the perimeter
        of the circle and return it."""
        return 2 * math.pi * self._radius


class Rectangle(Shape):
    """Rectangle class implements the abstract class Shape as a Rectangle.
    """

    def __init__(self, width, height):
        """the initializer method takes width and height of the Rectangle"""
        self._width = width
        self._height = height

    def area(self):
        """here we will implement the abstract method area to calculate
        the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """here we are implementing the abstract method perimeter
        of the class Shape to calc the perimeter of the rectangle."""
        return 2 * (self._width + self._height)


def shape_info(shape):
    """Function that accepts a Shape object and prints
    its area and perimeter"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
