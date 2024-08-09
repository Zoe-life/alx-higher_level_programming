#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute, 
type and value validation, optional size in the constructor,
and a public method to calculate the area.
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size  # Private attribute

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size  # Area formula: size squared