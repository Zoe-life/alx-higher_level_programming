#!/usr/bin/python3


class Rectangle(BaseGeometry):
    """
    Rectangle class inheriting from BaseGeometry with private width and height and validation.

    Attributes:
        __width (int): The private width of the rectangle (positive integer).
        __height (int): The private height of the rectangle (positive integer).
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle object.

        Args:
            width: The width of the rectangle (positive integer).
            height: The height of the rectangle (positive integer).

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than or equal to 0.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: A string representation of the rectangle in the format "[Rectangle] (<width>) / (<height>)"
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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