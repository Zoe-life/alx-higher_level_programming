#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute, 
type and value validation, optional size in the constructor,
a public method to calculate the area, a property for size, 
and a method to print a visual representation of the square.
"""


class Square:
    """
    A Square class representing a square.

    The size of the square is a private attribute for better data control.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints a visual representation of the square using the # character.
        """
        if self.size == 0:
            print()  # Empty line for size 0
        else:
            for _ in range(self.size):
                print("#" * self.size)