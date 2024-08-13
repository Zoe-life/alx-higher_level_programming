#!/usr/bin/python3


class BaseGeometry:
    """
    An enhanced BaseGeometry class with area raising an exception and a new integer validator method.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".

        This method is intended to be overridden in subclasses that provide specific area calculation logic.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer and checks if it's greater than 0.

        Args:
            name: A string representing the name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))