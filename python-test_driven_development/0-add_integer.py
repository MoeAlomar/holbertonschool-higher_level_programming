#!/usr/bin/python3
""" adds two integer """

def add_integer(a, b=98):
    """ 
    Args:
    a: integer or float variable
    b: integer or float variable
    
    """

    if not isinstance(a, int, float):
        raise TypeErro("a must be an integer")
    if not isinstance(b, int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
