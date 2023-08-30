class Node:
    """define class named Square """
    def __init__(self, data, next_node=None):
        """define privat size atturbute Square """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """define getter of atturbute """
        return (self.__data)

    @data.setter
    def data(self, value):
        """define setter of atturbute """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__size = value

    @property
    def next_node(self):
        """define getter of atturbute """
        return (self.__size)

    @next_node.setter
    def next_node(self, value):
        """define setter of atturbute """
        if not isinstance(value, Node) and value is not None
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""define class named SinglyLinkedList """


class SinglyLinkedList:
    """define class named SinglyLinkedList """
    def __init__(self):
        """define privat  atturbute """
    self.__head = None

    def sorted_insert(self, value):
        """define public print atturbute """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
