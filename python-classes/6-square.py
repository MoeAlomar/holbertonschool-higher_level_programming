#!/usr/bin/python3
"""Square module.

This module defines the Square class which models a geometric square.
It includes validation for the size attribute, along with methods
to compute the area and access or modify the size safely.
"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The length of a side of the square (private).
    """
    def __init__(self, size=0, position=(0,0)):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (int): two positive integer tuple.

        Raises:
            TypeError: If size is not an integer or if position value is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        for i in position:
            if not isinstance(i, int):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """A method to get the position tuple value.

        Returns:
            (int) tuple: two int tuple that determine the posi/
            tion of the square in the buffer (output)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """a setter method for the instance position tuple.
        
        Args:
            (tuple) value: is an integer tuple 
            to determine the position of square in output.

        Raises:
            TypeError: in case any value in position tuple is not an integer.     
        """
        for i in value:
            if not isinstance(i, int):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square in the shape of (#)

        if size empty it will print a newline
        otherwise it will print the square with (#), also now it will print space/
        s above and before the square depending on position tuple values.
        """
        for i in range(self.position[1]):
            print()
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(" " * self.position[0], end="")            
            for j in range(self.__size):
                print("#", end="")
            print()
