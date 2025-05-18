#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for add in (a_dictionary):
        new_dictionary[add] = a_dictionary[add] * 2
    return new_dictionary
