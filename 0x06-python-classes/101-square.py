#!/usr/bin/python3
"""
This module defines a Square class with private attributes size and position, 
type and value validation, optional size and position in the constructor,
a public method to calculate the area, properties for size and position, 
and methods to print a visual representation of the square.
"""


class Square:
    """
    A Square class representing a square.

    The size and position of the square are private attributes for better data control.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square (x, y). Defaults to (0, 0).

        Raises:
            TypeError: If size or any element in position is not an integer.
            ValueError: 
                - If size is less than 0.
                - If any element in position is less than or equal to 0.
        """
        self.__size = size
        self.position = position  # Call the property setter for position validation

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

    @property
    def position(self):
        """
        Retrieves the current position of the square.

        Returns:
            tuple: The position of the square (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): The new position of the square (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 integers.
            ValueError: If any element in value is less than or equal to 0.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(x <= 0 for x in value):
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints a visual representation of the square with the # character, 
        using the position attribute for placement.
        """
        if self.size == 0:
            print()  # Empty line for size 0
        else:
            for _ in range(self.position[1]):
                print()  # Print empty lines for vertical position

            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)  # Print rows with spaces

    def __str__(self):
        """
        String representation of the Square instance, calling my_print().

        Returns:
            str: The string representation of the square.
        """
        self.my_print()
        return ""  # Return an empty string to avoid extra newline