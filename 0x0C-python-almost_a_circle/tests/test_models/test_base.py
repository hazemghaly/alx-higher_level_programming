#!/usr/bin/python3
"""Unittest for
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class unit_test(unittest.TestCase):
    """define class named  unit_test """
    def json_string(self):
        """define return to_json_string """
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(to_json_string(r1),
                         [{"x": 2, "width": 10, "id": 1,
                           "height": 7, "y": 88}])

    def _Int_(self):
        """define return to_json_string """
        b1 = Base()
        self.assertEqual(__init__(b1), 1)


if __name__ == '__main__':
    unittest.main()
