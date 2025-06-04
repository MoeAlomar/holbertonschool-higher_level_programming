#!/usr/bin/python3
import pickle


""" this module is to serialize and deserialize a class using
pickling."""
class CustomObject:
    """
    this is the Customobject class
    that we will serialize and deserialize.
    """
    def __init__(self, name="", age=0, is_student=True):
        """ our init to set the attr with the given values.""" 
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display method that prints the instance in the following format:
        Example:
            Name: john
            Age: 25
            Is student: True
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")
    
    def serialize(self, filename):
        """
        this function serializes the instance of object 
        in the filename.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except(OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        this function deserializes as an object of the class.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return cls
                return None
        except(OSError, pickle.UnpicklingError, EOFError):
            return None
