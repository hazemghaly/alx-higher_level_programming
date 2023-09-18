#!/usr/bin/python3
"""define class named a rectangle """


from models.base import Base


class Rectangle(Base):
    """difine class named a rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """define getter of atturbute """
        return (self.__width)

    @width.setter
    def width(self):
        """define setter of atturbute """
        self.__width = width

    @property
    def height(self):
        """define getter of atturibute """
        return (self.__height)

    @height.setter
    def _height(self):
        """define setter of atturbute """
        self.__height = height

    @property
    def y(self):
        """define getter of atturibute """
        return (self.__y)

    @y.setter
    def y(self):
        """define setter of atturbute """
        self.__y = y

    @property
    def x(self):
        """define getter of atturibute """
        return (self.__x)

    @x.setter
    def x(self):
        """define setter of atturbute """
        self.__x = x
