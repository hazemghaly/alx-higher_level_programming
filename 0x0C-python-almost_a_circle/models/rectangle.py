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
        self.__width = value

    @property
    def height(self):
        """define getter of atturibute """
        return (self.__height)

    @height.setter
    def height(self, value):
        """define setter of atturbute """
        self.__height = value

    @property
    def y(self):
        """define getter of atturibute """
        return (self.__y)

    @y.setter
    def y(self, value):
        """define setter of atturbute """
        self.__y = value

    @property
    def x(self):
        """define getter of atturibute """
        return (self.__x)

    @x.setter
    def x(self, value):
        """define setter of atturbute """
        self.__x = value
