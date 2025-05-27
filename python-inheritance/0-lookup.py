#!/usr/bin/python3
"""here we define lookup method, a class that looks up for an object's method.
"""


def lookup(obj):
    """this class returns the list of all methods and attributes of an object.
    """
    return dir(obj)
