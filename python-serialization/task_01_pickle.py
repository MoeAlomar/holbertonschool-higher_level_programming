#!/usr/bin/python3
import pickle


"""This module provides functionality to serialize and deserialize
a class using pickling."""


class CustomObject:
    """A class to represent an object that can be serialized and deserialized."""
    
    def __init__(self, name="", age=0, is_student=True):
        """Initialize a CustomObject with name, age, and student status.
        
        Args:
            name (str): The name of the object (default: "").
            age (int): The age of the object (default: 0).
            is_student (bool): Whether the object is a student (default: True).
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in a formatted manner.
        
        Example:
            Name: John
            Age: 25
            Is student: True
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")
    
    def serialize(self, filename):
        """Serialize the instance to a file.
        
        Args:
            filename (str): The name of the file to store the serialized object.
        
        Returns:
            None: If serialization fails due to an error.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a file.
        
        Args:
            filename (str): The name of the file containing the serialized object.
        
        Returns:
            CustomObject: The deserialized instance if successful, else None.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.UnpicklingError, EOFError):
            return None
