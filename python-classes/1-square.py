#!/usr/bin/python3
"""This module is a subclass of the super class Square
it defines a square based on the super class"""
class Square(Square):
    """Here in this class we will define __init__ method which will assign the __size value"""
    def __init__(self,size):
        """This method will assign the private  attribute size value
        with the recieved size without any checking on value or type validation!!"""
        self.__size = size