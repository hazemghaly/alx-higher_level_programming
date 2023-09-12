#!/usr/bin/python3
"""difine class named a MyInt """


class MyInt(int):
    """difine class named a MyInt """
    def __eq__(self, vlu):
        """define return reversed oparetor representation """
        if(vlu == self.real):
            return (self.real != vlu)
    
    def __ne__(self, y):
        """define return reversed oparetor representation """
        return (self.real == y)
