#!/usr/bin/python3
"""
Module: 11-student.py

This module defines a Student class that represents a student with basic
personal information. The class provides functionality for serialization
and deserialization through dictionary conversion with optional attribute
filtering and reloading from dictionary data.

Classes:
    Student: A class representing a student with serialization.
             capabilities for first name, last name, and age attributes.
"""


class Student:
    """
    A class to represent a student with serialization capabilities.

    This class stores basic information about a student including their
    first name, last name, and age. It provides methods to serialize the
    student object to a dictionary format with optional attribute filtering
    and deserialize from a dictionary, implementing a complete serialization
    and deserialization mechanism.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.

        Example:
            >>> student = Student("John", "Doe", 20)
            >>> student.first_name
            'John'
            >>> student.age
            20
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        This method returns a dictionary representation of the student
        object. If attrs is provided as a list of strings, only the
        attributes specified in the list will be included in the returned
        dictionary. Otherwise, all attributes are retrieved.

        Args:
            attrs (list, optional): A list of attribute names (strings) to
                                   include in the returned dictionary If None
                                   all attributes are retrieved.

        Returns:
            dict: A dictionary containing the requested instance attributes
                  of the student object as key-value pairs.

        Example:
            >>> student = Student("Jane", "Smith", 22)
            >>> student.to_json()
            {'first_name': 'Jane', 'last_name': 'Smith', 'age': 22}
            >>> student.to_json(['first_name', 'age'])
            {'first_name': 'Jane', 'age': 22}
        """
        if isinstance(attrs, list):
            filtered_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    filtered_dict[key] = self.__dict__[key]
            return filtered_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance from a dictionary.

        This method updates the current student instance's attributes
        with values from the provided dictionary. Dictionary keys represent
        the public attribute names, and dictionary values represent the
        values to be assigned to those attributes.

        Args:
            json (dict): A dictionary where keys are public attribute names
                        and values are the corresponding attribute values
                        to set on the student instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
