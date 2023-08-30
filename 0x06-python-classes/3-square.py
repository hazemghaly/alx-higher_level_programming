#!/usr/bin/python3
"""define class named Square """


class Square:
    """define class named Square """
    def __init__(self, size=0):
        """define privat size atturbute Square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """define public aera atturbute """
        return (self.__size ** 2)
