#!/usr/bin/python3
"""define class named a Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """difine class named a rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """define getter of atturibute """
        return (self.width)

    @size.setter
    def size(self, value):
        """define setter of atturbute """
        self.width = value
        self.height = value

    def __str__(self):
        """define public overriding  atturbute """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """define public argument  atturbute """
        if args and len(args) != 0:
            i = 1
            for arg in args:
                if i == 1:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 2:
                    self.size = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """define dictionary reper """
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
