class Node:
    """
    A Node class representing a single node in a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The data value stored in the node.
            next_node (Node, optional): The next node in the linked list. Defaults to None.

        Raises:
            TypeError:
                - If data is not an integer.
                - If next_node is not None or a Node object.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data value stored in the node.

        Returns:
            int: The data value.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data value stored in the node with validation.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            Node: The next node, or None if it's the last node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list with validation.

        Args:
            value (Node, optional): The new next node. Defaults to None.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """
    A SinglyLinkedList class representing a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance.
        """
        self.head = None  # Private attribute, no getter or setter

    def __str__(self):
        """
        String representation of the linked list, printing each node's data on a new line.

        Returns:
            str: The string representation of the list.
        """
        output = ""
        current = self.head
        while current:
            output += f"{current.data}\n"
            current = current.next_node
        return output[:-1]  # Remove the trailing newline

    def sorted_insert(self, value):
        """
        Inserts a new node with the specified value into the linked list 
        in the correct sorted position (ascending order).

        Args:
            value (int): The value for the new node.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        previous = None
        while current and current.data < value:
            previous = current
            current = current.next_node

        if previous is None:
            new_node.next_node = self.head
            self.head = new_node
        else:
            new_node.next_node = current
            previous.next_node = new_node