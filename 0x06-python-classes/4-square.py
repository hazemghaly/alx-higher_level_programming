#!/usr/bin/python3
"""define class named Square """


class Square:
    """define class named Square """
    def __init__(self, size=0):
        """define privat size atturbute Square """
        self.__size = size

    @property
    def size(self):
        """define getter of atturbute """
        return (self.__size)

    @size.setter
    def size(self, value):
        """define setter of atturbute """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """define public aera atturbute """
        return (self.__size ** 2)
