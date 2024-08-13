#!/usr/bin/python3


class Square(Rectangle):
    """
    Square class inheriting from Rectangle with a private size attribute.

    Attributes:
        __size (int): The private size of the square (positive integer).
    """

    def __init__(self, size):
        """
        Initializes a new Square object.

        Args:
            size: The size of the square (positive integer).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        This method overrides the parent class method as the area of a square is simply size * size.

        Returns:
            int: The area of the square (size * size).
        """

        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the Square object.

        This method inherits the format from the parent class and uses the size attribute.

        Returns:
            str: A string representation of the square in the format "[Square] (<size>) / (<size>)"
        """

        return "[Square] {}/{}".format(self.__size, self.__size)