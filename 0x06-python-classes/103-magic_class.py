class MagicClass:
    """
    A MagicClass representing a circle with a radius attribute.
    """

    def __init__(self, radius):
        """
        Initializes a new MagicClass instance.

        Args:
            radius (number): The radius of the circle.

        Raises:
            TypeError: If radius is not a number (int or float).
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius**2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius