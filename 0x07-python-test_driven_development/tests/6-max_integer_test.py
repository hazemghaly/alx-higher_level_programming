#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """define class named TestMaxInteger """
    def Test_Maxorder(self):
        """Test list of integers."""
        L = [1, 2, 3, 4]
        self.assertEqual(max_integer(L), 4)

    def Test_Max(self):
        """Test list of integers."""
        o = [1, 2, 4, 3]
        self.assertEqual(max_integer(o), 4)

    def Test_p(self):
        """Test list of integers."""
        p = []
        self.assertEqual(max_integer(p), None)

    def Test_ele(self):
        """Test list of integers."""
        ele = [9]
        self.assertEqual(max_integer(ele), 9)

    def Test_floats(self):
        """Test list of integers."""
        f = [1.9, 2.5, 6.5]
        self.assertEqual(max_integer(f), 6.5)

if __name__ == '__main__':
    unittest.main()
