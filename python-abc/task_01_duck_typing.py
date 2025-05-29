#!/usr/bin/python3
from abc import ABC, abstractmethod
"""in this module we should try duck typing by creating an abstract class
and implementing it through different classes with the same methods."""


class Shape(ABC):
    """Shape is our abstract class that we will implement
    and all its methods are abstract."""
    @abstractmethod
    def area(self):
        """area is a an abstract method to be implemented."""
        ...

    @abstractmethod
    def perimeter(self):
        """an abstract method to calc the perimeter"""
        ...


class Cricle(Shape):
    """Circle is a class that implements the abstract Shape class."""

    def __init__(self, r):
        """initializer method of circle class
        Args:
            r: is an integer and refers to the 'radius' of the circle.
        """
        self._r = r

    def area(self):
        """here we are implementing the area method for circle class
        to calculate the area of the circle and return it"""
        return 3.14 * (r**2)

    def perimeter(self):
        """this method is implemented to calculate the perimeter
        of the circle and return it."""
        return 2 * 3.14 * r


class Rectangle(Shape):
    """Rectangle class implements the abstract class Shape as a Rectangle."""

    def __init__(self, height, width):
        """the initializer method takes width and height of the Rectangle"""
        self._height = height
        self._width = width

    def area(self):
        """here we will implement the abstract method area to calculate
        the area of the rectangle."""
        return self._height * self._width

    def perimeter(self):
        """here we are implementing the abstract method perimeter
        of the class Shape to calc the perimetr of the rectangle."""
        return 2 * (self._height + self._width)
