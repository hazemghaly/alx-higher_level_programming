#!/usr/bin/python3
"""difine class named a BaseGeometry """


class BaseGeometry:
    """difine class named a BaseGeometry """

    def integer_validator(self, name, value):
        """define atturbute """
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")

    def area(self):
        """define public area atturbute """
        raise Exception("area() is not implemented")


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
        return (f'[Rectangle] {self.__width}/{self.__height}')
