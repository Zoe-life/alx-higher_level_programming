#!/usr/bin/python3


class MyInt(int):
    """
    MyInt class inherits from int and overrides comparison operators for a rebellious behavior.
    """

    def __eq__(self, other):
        """
        Overrides the default equality operator (`==`) to return the opposite of the original comparison.

        Args:
            other: The object to compare with.

        Returns:
            bool: False if the objects are equal, True otherwise.
        """

        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Overrides the default inequality operator (`!=`) to return the opposite of the original comparison.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """

        return not super().__ne__(other)