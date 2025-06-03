#!/usr/bin/python3
"""
Module: student_filtered

This module defines a Student class that represents a student with basic
personal information. The class provides functionality to convert student
instances to dictionary format with optional attribute filtering for
JSON serialization.

Classes:
    Student: A class representing a student with first name, last name, and age,
             with support for filtered dictionary conversion.
"""


class Student:
    """
    A class to represent a student with filtering capabilities.
    
    This class stores basic information about a student including their
    first name, last name, and age. It provides methods to convert the
    student object to a dictionary format with optional attribute filtering,
    suitable for JSON serialization.
    
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
        Convert the Student instance to a dictionary with optional filtering.
        
        This method returns a dictionary representation of the student
        object. If attrs is provided as a list, only the attributes
        specified in the list will be included in the returned dictionary.
        If attrs is None or not a list, all instance attributes are returned.
        
        Args:
            attrs (list, optional): A list of attribute names to include
                                   in the returned dictionary. If None,
                                   all attributes are included.
        
        Returns:
            dict: A dictionary containing the requested instance attributes
                  of the student object as key-value pairs.
        
        Example:
            >>> student = Student("Jane", "Smith", 22)
            >>> student.to_json()
            {'first_name': 'Jane', 'last_name': 'Smith', 'age': 22}
            >>> student.to_json(['first_name', 'age'])
            {'first_name': 'Jane', 'age': 22}
            >>> student.to_json(['first_name', 'nonexistent'])
            {'first_name': 'Jane'}
        """
        if isinstance(attrs, list):
            filtered_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    filtered_dict[key] = self.__dict__[key]
            return filtered_dict
        return self.__dict__
