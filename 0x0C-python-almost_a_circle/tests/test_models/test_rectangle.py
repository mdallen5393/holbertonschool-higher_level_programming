#!/usr/bin/python3
"""
Unittest module for Rectangle class.
"""
from io import StringIO
from unittest.mock import patch
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
        with self.assertRaises(ValueError):
            Rectangle(-1, 1, 0, 0, 100)
        with self.assertRaises(ValueError):
            Rectangle(1, -1, 0, 0, 100)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1, 0, 100)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -1, 100)
        with self.assertRaises(TypeError):
            Rectangle("1", 1, 0, 0, 100)
        with self.assertRaises(TypeError):
            Rectangle(1, "1", 0, 0, 100)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "0", 0, 100)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 0, "0", 100)

    def test_area(self):
        """
        Method for testing the area method of the Rectangle class.
        """
        self.assertEqual(self.rect1.area(), 1)

        self.rect2 = Rectangle(5, 2, 0, 0, 200)
        self.assertEqual(self.rect2.area(), 10)

        del self.rect2

    def test_display(self):
        """
        Method for testing the display method of the Rectangle class.
        """
        with patch('sys.stdout', new = StringIO()) as fake_out:
            self.rect1.display()
            self.assertEqual(fake_out.getvalue(), '#\n')
            Rectangle(4, 2, 1, 3, 200).display()
            output = "#\n\n\n\n ####\n ####\n"
            self.assertEqual(fake_out.getvalue(), output)

    def test_str(self):
        """
        Method for testing the __str__ method of the Rectangle class.
        """
        self.assertEqual(str(self.rect1), '[Rectangle] (100) 0/0 - 1/1')

    def test_update(self):
        """
        Method for testing the update method of the Rectangle class.
        """
        self.rect1.update(89, 2, 3, 4, 5)
        self.assertEqual(self.rect1.id, 89)
        self.assertEqual(self.rect1.width, 2)
        self.assertEqual(self.rect1.height, 3)
        self.assertEqual(self.rect1.x, 4)
        self.assertEqual(self.rect1.y, 5)

        self.rect1.update(id=100, width=1, height=1, x=0, y=0)
        self.assertEqual(self.rect1.id, 100)
        self.assertEqual(self.rect1.width, 1)
        self.assertEqual(self.rect1.height, 1)
        self.assertEqual(self.rect1.x, 0)
        self.assertEqual(self.rect1.y, 0)

    def test_to_dictionary(self):
        """
        Method for testing the to_dictionary method of the Rectangle
        class.
        """
        rect1_dict = {'x': 0, 'y': 0, 'id': 100, 'height': 1, 'width': 1}
        self.assertEqual(self.rect1.to_dictionary(), rect1_dict)
        self.assertTrue(type(self.rect1.to_dictionary()), dict)

if __name__ == '__main__':
    unittest.main()
