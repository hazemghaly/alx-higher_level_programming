#!/usr/bin/python3
"""define class named a rectangle """


from models.base import Base


class Rectangle(Base):
    """difine class named a rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

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

    @property
    def height(self):
        """define getter of atturibute """
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
    def y(self):
        """define getter of atturibute """
        return (self.__y)

    @y.setter
    def y(self, value):
        """define setter of atturbute """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """define getter of atturibute """
        return (self.__x)

    @x.setter
    def x(self, value):
        """define setter of atturbute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """define public area atturbute """
        return (self.__width * self.__height)
