#!/usr/bin/python3
from abc import ABC, abstractmethod
"""in this module we should create an abstract class Animal
and implement it and its method through two diff classes."""


class Animal(ABC):
    """an abstract class to be implemented by other classes later."""
    @abstractmethod
    def sound(self):
        ...


class Dog(Animal):
    """this class of a cat return moew and implements Abstract class Animal."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """this class of a cat return moew and implements Abstract class Animal."""

    def sound(self):
        return "Meow"
