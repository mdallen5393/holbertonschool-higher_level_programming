#!/usr/bin/python3
"""
Unittest module for Square class.
"""
import unittest
from models.square import Square

class test_square(unittest.TestCase):
    """
    Class test_square that provides unit testing for the `Square`
    class.
    """
    @classmethod
    def setUpClass(cls):
        """
        setUp method for testing the Square class.
        """
        cls.square1 = Square(1, 0, 0, 100)

    @classmethod
    def tearDownClass(cls):
        """
        tearDown method for testing the Square class.
        """
        del cls.square1
        return super().tearDownClass()

    def test_init(self):
        """
        Method for testing initialization of the Square class.
        """
        self.assertEqual(self.square1.id, 100)
        self.assertEqual(self.square1.size, 1)
        self.assertEqual(self.square1.x, 0)
        self.assertEqual(self.square1.y, 0)
        with self.assertRaises(ValueError):
            Square(-1, 0, 0, 100)
        with self.assertRaises(ValueError):
            Square(1, -1, 0, 100)
        with self.assertRaises(ValueError):
            Square(1, 0, -1, 100)
        with self.assertRaises(TypeError):
            Square("1", 0, 0, 100)
        with self.assertRaises(TypeError):
            Square(1, "0", 0, 100)
        with self.assertRaises(TypeError):
            Square(1, 0, "0", 100)

    def test_str(self):
        """
        Method for testing the __str__ method of the Square class.
        """
        self.assertEqual(str(self.square1), '[Square] (100) 0/0 - 1')

    def test_update(self):
        """
        Method for testing the update method of the Square class.
        """
        self.square1.update(89, 2, 3, 4)
        self.assertEqual(self.square1.id, 89)
        self.assertEqual(self.square1.size, 2)
        self.assertEqual(self.square1.x, 3)
        self.assertEqual(self.square1.y, 4)
        self.square1.update(size=1, y=0, x=0, id=100)
        self.assertEqual(self.square1.id, 100)
        self.assertEqual(self.square1.size, 1)
        self.assertEqual(self.square1.x, 0)
        self.assertEqual(self.square1.y, 0)

    def test_to_dictionary(self):
        """
        Method for testing the to_dictionary method of the Square
        class.
        """
        square1_dict = {'x': 0, 'y': 0, 'id': 100, 'size': 1}
        self.assertEqual(self.square1.to_dictionary(), square1_dict)
        self.assertTrue(type(self.square1.to_dictionary()), dict)

if __name__ == '__main__':
    unittest.main()
