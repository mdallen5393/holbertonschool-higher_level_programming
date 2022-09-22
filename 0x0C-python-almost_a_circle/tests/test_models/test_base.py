#!/usr/bin/python3
"""
Unittest module for Base class.
"""
import unittest
from models.base import Base as Base
from models.rectangle import Rectangle as Rectangle
from models.square import Square as Square


class BaseTests(unittest.TestCase):
    """
    Class BaseTests that provides unit testing for the `Base` class.
    """
    @classmethod
    def setUpClass(cls):
        """
        setUp method for testing the Base class.
        """
        cls.base1 = Base()
        cls.rect1 = Rectangle(1, 1, 0, 0, 200)
        cls.square1 = Square(1, 0, 0, 300)

    @classmethod
    def tearDownClass(cls):
        """
        tearDown method for testing the Base class.
        """
        del cls.base1
        del cls.rect1
        del cls.square1
        # return super().tearDown()

    def test_init(self):
        """
        Method for testing initialization of the Base class.
        """
        self.assertEqual(self.base1.id, 1)

        self.base2 = Base(2)
        self.assertEqual(self.base2.id, 2)

        self.base3 = Base()
        self.assertEqual(self.base3.id, 2)

        self.assertEqual(self.base2.id, self.base3.id)

        """
        There is no sanitization for id: it can be any type,
        though it is assumed to be an integer
        <<Possibly Not Required>>
        """
        self.base4 = Base("stuff")
        self.assertEqual(self.base4.id, 'stuff')

        del self.base2
        del self.base3
        del self.base4

    def test_to_json_string(self):
        """
        Method for testing the to_json_string method in the Base
        class.
        """
        dictionary_r = self.rect1.to_dictionary()
        json_dictionary_r = self.rect1.to_json_string([dictionary_r])
        dicStr = '[{"x": 0, "y": 0, "id": 200, "height": 1, "width": 1}]'
        self.assertEqual(json_dictionary_r, dicStr)

        dictionary_s = self.square1.to_dictionary()
        json_dictionary_s = self.square1.to_json_string([dictionary_s])
        dicStr = '[{"id": 300, "x": 0, "size": 1, "y": 0}]'
        self.assertEqual(json_dictionary_s, dicStr)

        self.assertRaises(TypeError, self.square1.to_json_string, dictionary_s)
        self.assertRaises(TypeError, self.square1.to_json_string, [1])

        dicList = [self.square1.to_dictionary(), self.rect1.to_dictionary()]
        dicStr = '[{"id": 300, "x": 0, "size": 1, "y": 0}, ' \
            + '{"x": 0, "y": 0, "id": 200, "height": 1, "width": 1}]'
        self.assertEqual(self.square1.to_json_string(dicList), dicStr)

        self.assertEqual(self.square1.to_json_string(None), "[]")
        self.assertEqual(self.square1.to_json_string([]), "[]")


