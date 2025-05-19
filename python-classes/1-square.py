#!/usr/bin/python3
"""This module defines a Square class with a private size attribute.

The size of the square is stored privately to enforce encapsulation.
"""
class Square():
    """Here in this class we will define __init__ method which will assign the __size value"""
    def __init__(self,size):
        """This method will assign the private  attribute size value
        with the recieved size without any checking on value or type validation!!
        Args:
        size: the size of the square should be an integer"""
        self.__size = size