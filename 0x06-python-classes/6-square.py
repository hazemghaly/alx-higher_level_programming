#!/usr/bin/python3
"""define class named Square """


class Square:
    """define class named Square """
    def __init__(self, size=0, position=(0, 0)):
        """define privat size atturbute Square """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """define getter of atturbute """

    @position.setter
    def position(self, value):
        """define setter of atturbute """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """define public area atturbute """
        return (self.__size ** 2)

    def my_print(self):
        """define public print atturbute """
        if self.__size == 0:
            print("")
            return
        for a in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for h in range(0, self.__position[0]):
                print("", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
