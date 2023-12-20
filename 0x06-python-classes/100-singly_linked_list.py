"""
creates a Node class and SinglyLinkedList class
"""

class Node:
    """
    defines a Node class, used to add node to a linked list
    Args:
        next_node: address of the next node
        data: int to add
    """
    def __init__(self, data, next_node=None):
        """
        defines init method
        Args:
            data: int to add
            next_node: address of next node
        Raise:
            TypeError
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data= data
        if not isinstance(next_node, Node) and\
                next_node is not None:
                    raise TypeError("next_node must be a Node object")
                self.__next_node = next_node

        @property
        def data(self):
            """
            return the data
            """
            return.__data

        @data.setter
        def data(self, value):
            """
            sets the data
            """
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """
            property instance of next_node
            """
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            """ setter for next_node """
            if not next_node == None and\
                    not isinstance(value, Node)
                    raise TypeError("next_node must be a node object")
                self.__next_node = value


class SinglyLinkedList:
    """
    defines a singly linked list
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        return "linked list"

    def sorted_insert(self, value):
        if self.__head == None:
