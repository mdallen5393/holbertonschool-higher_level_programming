#!/usr/bin/python3
"""
Unittest module for Rectangle class.
"""
import unittest
from models.base import Base

class test_rectangle(unittest.TestCase):
    """
    Class test_rectangle that provides unit testing for the `Rectangle`
    class.
    """
    def test_values(self):
        """
        Value unit tests.
        """
        base1 = Base(10)
        # TODO: add self.assertEqual(max_integer("String"), 't')
        pass

if __name__ == '__main__':
    unittest.main()
