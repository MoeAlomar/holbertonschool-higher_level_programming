#!/usr/bin/python3
"""A class that checks if an object is of the same class"""


def inherits_from(obj, a_class):
    """this function checks if the
    provided function is of an inherited class provided but
    not from the same class

    Args:
        obj: is an object from any type.
        a_class: a class that returns true of the obj is instance of it.

    Returns:
        True: if the class has this object.
        False: otherwisse.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
