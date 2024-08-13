#!/usr/bin/python3


class Rectangle:
    """Defines a rectangle with private attributes for width and height."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the private width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute, validating it's an integer and non-negative.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the private height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute, validating it's an integer and non-negative.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value