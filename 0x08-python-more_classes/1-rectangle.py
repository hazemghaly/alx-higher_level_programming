#!/usr/bin/python3
"""define class named a rectangle """


class Rectangle:
    """difine class named a rectangle """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """define getter of atturbute """
        return (self.__height)

    @height.setter
    def height(self, value):
        """define setter of atturbute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """define getter of atturbute """
        return (self.__width)

    @width.setter
    def width(self, value):
        """define setter of atturbute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
