#!/usr/bin/python3
"""import relevant modules"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """tests for the class Review"""
    def setUp(self):
        """set up method"""
        self.review = Review()

    def testClassPresent(self):
        """chck if class exists"""
        self.assertEqual(
                str(type(self.review)), "<class 'models.review.Review'>"
                )

    def testAttributesPresent(self):
        """check if attrs are present"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertTrue(hasattr(self.review, 'user_id'))

    def testAttrTypes(self):
        """check for the right attr types"""
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.user_id, str)

    def testIsInstance(self):
        """check if class is instance of BaseModel"""
        self.assertIsInstance(self.review, BaseModel)
