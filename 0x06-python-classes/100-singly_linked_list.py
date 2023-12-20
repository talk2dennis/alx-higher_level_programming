#!/usr/bin/python3
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
        self.data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.next_node = next_node

        @property
        def data(self):
            """
            defines getter which returns the data
            """
            return self.__data

        @data.setter
        def data(self, value):
            """
            sets the data
            Args:
                value: int to add
            Raise:
                TypeError if int was not provided
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
            """
            setter for next_node
            Args:
                value: int to add
            """
            if next_node is not None and \
                    not isinstance(value, Node):
                raise TypeError("next_node must be a node object")
            self.__next_node = value


class SinglyLinkedList:
    """
    defines a singly linked list
    """
    def __init__(self):
        """
        defines init method
        """
        self.__head = None

    def __str__(self):
        """
        defines str representation of the class
        """
        tmp = self.__head
        new_list = []
        while tmp:
            new_list.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(new_list))

    def sorted_insert(self, value):
        """
        defines sorted_insert method which inserts node in sorted order
        Args:
            value: int to add
        """
        tmp = Node(value)
        if self.__head is None:
            self.__head = tmp
        elif self.__head.data > value:
            tmp.next_node = self.__head
            self.__head = tmp
        else:
            aux = self.__head
            while aux.next_node and aux.next_node.data < value:
                aux = aux.next_node
            tmp.next_node = aux.next_node
            aux.next_node = tmp
