#!/usr/bin/python3


class Rectangle:
    """Defines a rectangle with private attributes for width and height."""

    number_of_instances = 0
    print_symbol = "#"

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
        """Returns a string representation of the rectangle using the print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        representation = ""
        symbol = self.print_symbol
        if isinstance(symbol, str):  # Handle single character symbol
            for _ in range(self.height):
                representation += symbol * self.width + "\n"
        else:  # Handle iterable symbol (like a list)
            symbol_length = len(symbol)
            for i in range(self.height):
                representation += "".join(symbol[j % symbol_length] for j in range(self.width)) + "\n"
        return representation[:-1]

    def __repr__(self):
        """Returns a string representation that can be used to recreate the object with eval()."""
        return f"Rectangle(width={self.width}, height={self.height})"

    def __del__(self):
        """Prints a message and decrements the number of instances when deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles based on area and returns the larger or equal one.

        Args:
            rect_1: An instance of Rectangle.
            rect_2: An instance of Rectangle.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            The rectangle with the larger area, or rect_1 if they have the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2