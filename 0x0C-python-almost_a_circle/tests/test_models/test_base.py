#!/usr/bin/python3
"""
Unittest module for Base class.
"""
import unittest
# TODO: max_integer = __import__('6-max_integer').max_integer
Base = __import__('base').Base


class test_base(unittest.TestCase):
    """
    Class test_base that provides unit testing for the `Base` class.
    """
    def test_values(self):
        """
        Value unit tests.
        """
        # TODO: add self.assertEqual(max_integer("String"), 't')
        pass

if __name__ == '__main__':
    unittest.main()
