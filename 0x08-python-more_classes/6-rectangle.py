#!/usr/bin/python3


class Rectangle:
    """Defines a rectangle with private attributes for width and height."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height.

        Increments the number of instances.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle.

        If width or height is 0, the perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle using the # character."""
        if self.width == 0 or self.height == 0:
            return ""
        representation = ""
        for _ in range(self.height):
            representation += "#" * self.width + "\n"
        return representation[:-1]

    def __repr__(self):
        """Returns a string representation that can be used to recreate the object with eval()."""
        return f"Rectangle(width={self.width}, height={self.height})"

    def __del__(self):
        """Prints a message and decrements the number of instances when deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1