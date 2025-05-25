#!/usr/bin/python3
"""square module.

This module defines a Square class that represents a square
by its size and position,
and allows computation of its area and visual representation
with the `#` character.
"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): Size of one side of the square (private).
        __position (tuple): Position (horizontal and vertical offset)
        used when printing the square.
    """
    def __init__(self, size=0, position=(0,0)):
        """Initializes a new Square instance.

        Args:
            size (int, optional): Size of the square (default is 0).
            position (tuple, optional): Position offset when printing
            (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer, or if position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in position:
            if not isinstance(i, int) or i < 0:
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
            TypeError: in case any value in position tuple is not an integer or value < 2.     
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or i < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the `#` character based on its
        size and position.

        If size is 0, prints an empty line.
        The square is printed using `position[0]` spaces (horizontal offset)
        and `position[1]` newlines (vertical offset).
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
