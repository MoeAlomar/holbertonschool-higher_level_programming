#!/usr/bin/python3
def add_integer(a, b=98):
    """ adds two integer """

    if not isinstance(a, int, float):
        raise TypeErro("a must be an integer")
    if not isinstance(b, int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
