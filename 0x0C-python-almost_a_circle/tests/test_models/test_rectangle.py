#!/usr/bin/python3
"""
Unittest module for Rectangle class.
"""
import unittest
from models.rectangle import Rectangle

class test_rectangle(unittest.TestCase):
    """
    Class test_rectangle that provides unit testing for the `Rectangle`
    class.
    """
    @classmethod
    def setUpClass(cls):
        """
        setUp method for testing the Rectangle class.
        """
        cls.rect1 = Rectangle(1, 1, 0, 0, 100)

    @classmethod
    def tearDownClass(cls):
        """
        tearDown method for testing the Rectangle class.
        """
        del cls.rect1
        return super().tearDownClass()

    def test_init(self):
        """
        Method for testing initialization of the Rectangle class.
        """
        self.assertEqual(self.rect1.id, 100)
        self.assertEqual(self.rect1.width, 1)
        self.assertEqual(self.rect1.height, 1)
        self.assertEqual(self.rect1.x, 0)
        self.assertEqual(self.rect1.y, 0)

    def test_area(self):
        """
        Method for testing the area method of the Rectangle class.
        """
        pass

    def test_display(self):
        """
        Method for testing the display method of the Rectangle class.
        """
        pass

    def test_str(self):
        """
        Method for testing the __str__ method of the Rectangle class.
        """
        pass

    def test_update(self):
        """
        Method for testing the update method of the Rectangle class.
        """
        pass

    def test_to_dictionary(self):
        """
        Method for testing the to_dictionary method of the Rectangle
        class.
        """
        pass


if __name__ == '__main__':
    unittest.main()
