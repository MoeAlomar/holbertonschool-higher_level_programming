#!/usr/bin/python3
"""
Module: class_to_obj

This module provides functionality to convert class instances to dictionary objects.
It contains a utility function that extracts the instance attributes of an object
and returns them as a dictionary representation.

Functions:
    class_to_obj(obj): Converts an object's instance attributes to a dictionary.
"""


def class_to_json(obj):
    """
    Convert an object's instance attributes to a dictionary.
    
    This function takes any object and returns a dictionary containing
    all of its instance attributes (stored in the object's __dict__).
    This is commonly used for serialization purposes, such as converting
    objects to JSON format.
    
    Args:
        obj: Any object instance that has a __dict__ attribute.
    
    Returns:
        dict: A dictionary containing the object's instance attributes
              as key-value pairs.
    
    Example:
        >>> class Person:
        ...     def __init__(self, name, age):
        ...         self.name = name
        ...         self.age = age
        >>> person = Person("Alice", 30)
        >>> class_to_obj(person)
        {'name': 'Alice', 'age': 30}
    """
    return obj.__dict__
