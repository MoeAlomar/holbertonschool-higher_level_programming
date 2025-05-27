#!/usr/bin/python3
"""A class that checks if an object is of the same class"""


def is_kind_of_class(obj, a_class):
    """this function checks if the
    provided function is of the same class provided

    Args:
        obj: is an object from any type.
        a_class: a class that returns true of the obj is instance of it.

    Returns:
        True: if the class has this object.
        False: otherwisse.
    """
    return isinstance(obj, a_class)
