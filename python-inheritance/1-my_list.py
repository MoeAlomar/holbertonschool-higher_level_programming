#!/usr/bin/python3
"""Mylist class is recieving a list obj to be sorted and printed
using sort function in python.
"""


class MyList(list):
    """here we are recieving list and sort it using sort function in python
    """
    my_list = list

    def print_sorted(self):
        """
        print_sorted is a method that will print the list of the class
        """
        sorted_mylist = self.copy()
        sorted_mylist.sort()
        print(sorted_mylist)
