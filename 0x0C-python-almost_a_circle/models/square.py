#!/usr/bin/python3
"""define class named a Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """difine class named a rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """define public overriding  atturbute """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.width))
