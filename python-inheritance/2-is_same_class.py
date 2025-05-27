#!/usr/bin/python3
"""A class that checks if an object is of the same class"""


def is_same_class(obj, a_class):
    """this function checks if the
    provided function is of the same class provided

    Args:
        obj: is an object from any type.
        a_class: a class that returns true of the obj is instance of it.

    Returns:
        True: if the class has this object.
        False: otherwisse.
    """
    return type(obj) is a_class
