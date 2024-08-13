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

        return "[Rectangle] {}/{}".format(self.__width, self.__height)  # Using f-strings