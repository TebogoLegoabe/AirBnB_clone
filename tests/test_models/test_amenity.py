#!/usr/bin/python3
"""import relevant modules"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """tests for the class Amenity"""
    def setUp(self):
        """set up method"""
        self.amenity = Amenity()

    def testClassPresent(self):
        """chck if class exists"""
        self.assertEqual(
                str(type(self.amenity)), "<class 'models.amenity.Amenity'>"
                )

    def testAttributesPresent(self):
        """check if attrs are present"""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def testAttrTypes(self):
        """check for the right attr types"""
        self.assertIsInstance(self.amenity.name, str)

    def testIsInstance(self):
        """check if class is instance of BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)
