#!/usr/bin/python3
"""
Module: student

This module defines a Student class that represents a student with basic
personal information. The class provides functionality to convert student
instances to dictionary format for JSON serialization.

Classes:
    Student: A class representing a student with first name, last name, and age.
"""


class Student:
    """
    A class to represent a student.
    
    This class stores basic information about a student including their
    first name, last name, and age. It provides methods to convert the
    student object to a dictionary format suitable for JSON serialization.
    
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

    def to_json(self):
        """
        Convert the Student instance to a dictionary.
        
        This method returns a dictionary representation of the student
        object containing all instance attributes. This is useful for
        JSON serialization or when you need to convert the object to
        a format that can be easily serialized.
        
        Returns:
            dict: A dictionary containing all instance attributes of the
                  student object as key-value pairs.
        
        Example:
            >>> student = Student("Jane", "Smith", 22)
            >>> student.to_json()
            {'first_name': 'Jane', 'last_name': 'Smith', 'age': 22}
        """
        return self.__dict__
