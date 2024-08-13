#!/usr/bin/python3


class MyList(list):
    """
    MyList class inherits from the built-in list class and provides a method for printing the list in sorted order.

    Attributes:
        Inherits all attributes from the list class.

    Methods:
        print_sorted(self): Prints the list elements in ascending order without modifying the original list.
    """

    def print_sorted(self):
        """
        Prints the elements of the MyList object in ascending order.

        This method creates a copy of the list, sorts it, and then prints the sorted elements.
        The original list remains unchanged.
        """

        sorted_list = sorted(self)  # Create a sorted copy
        print(sorted_list)