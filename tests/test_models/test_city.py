#!/usr/bin/python3
"""import relevant modules"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """tests for the class City"""
    def setUp(self):
        """set up method"""
        self.c = City()

    def testClassPresent(self):
        """chck if class exists"""
        self.assertEqual(str(type(self.c)), "<class 'models.city.City'>")

    def testAttributesPresent(self):
        """check if attrs are present"""
        self.assertTrue(hasattr(self.c, 'state_id'))
        self.assertTrue(hasattr(self.c, 'name'))

    def testAttrTypes(self):
        """check for the right attr types"""
        self.assertIsInstance(self.c.state_id, str)
        self.assertIsInstance(self.c.name, str)

    def testIsInstance(self):
        """check if class is instance of BaseModel"""
        self.assertIsInstance(self.c, BaseModel)
