#!/usr/bin/python3
"""define class named a rectangle """


class Rectangle:
    """difine class named a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.__height = height
        self.__width = width

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

    def area(self):
        """define public area atturbute """
        return (self.__width * self.__height)

    def perimeter(self):
        """define public perimeter atturbute """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        s = []
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(self.__height):
            [s.append(str(self.print_symbol))for j in range(self.__width)]
            if i != self.__height - 1:
                s.append("\n")
        return ("".join(s))

    def __repr__(self):
        return (f'Rectangle({self.width}, {self.height})')

    def __del__(cls):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
