#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute, 
type and value validation, optional size in the constructor,
a public method to calculate the area, a property for size, 
and comparison operators for Square instances based on area.
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
            size (number, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the current size of the square.

        Returns:
            float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (number): The new size of the square.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Implements the equal to operator (==) for Square instances.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the areas of both squares are equal, False otherwise.
        """
        if not isinstance(other, Square):
            return False
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Implements the not equal to operator (!=) for Square instances.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the areas of both squares are not equal, False otherwise.
        """
        return not self == other

    def __lt__(self, other):
        """
        Implements the less than operator (<) for Square instances.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area of the current square is less than the other square, False otherwise.
        """
        if not isinstance(other, Square):
            return False
        return self.area() < other.area()

    def __le__(self, other):
        """
        Implements the less than or equal to operator (<=) for Square instances.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area of the current square is less than or equal to the other square, False otherwise.
        """
        return self < other or self == other

    def __gt__(self, other):
        """
        Implements the greater than operator (>) for Square instances.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area of the current square is greater than the other square, False otherwise.
        """
        return not self <= other

    def __ge__(self, other):
        """
        Implements the greater than or equal to operator (>=) for Square instances.

        Args:
            other (Square): The other Square instance to compare with.

        Returns:
            bool: True if the area of the current square is greater than or equal to the other square, False otherwise.
        """
        return self > other or self == other