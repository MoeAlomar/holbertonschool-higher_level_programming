#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    return del a_dictionary[key] if key in a_dictionary else a_dictionary
