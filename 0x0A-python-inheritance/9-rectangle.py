#!/usr/bin/python3
"""difine class named a BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """difine class named a rectangle """

    def __init__(self, width, height):
        """define atturbute """
        super().integer_validator(width, height)
        self.__height = height
        self.__width = width

    def area(self):
        """define public area atturbute """
        return (self.__width * self.__height)

    def __str__(self):
        """define return str representation """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
