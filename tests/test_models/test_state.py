#!/usr/bin/python3
"""import relevant modules"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """tests for the class State"""
    def setUp(self):
        """set up method"""
        self.state = State()

    def testClassPresent(self):
        """chck if class exists"""
        self.assertEqual(str(type(self.state)), "<class 'models.state.State'>")

    def testAttributesPresent(self):
        """check if attrs are present"""
        self.assertTrue(hasattr(self.state, 'name'))

    def testAttrTypes(self):
        """check for the right attr types"""
        self.assertIsInstance(self.state.name, str)

    def testIsInstance(self):
        """check if class is instance of BaseModel"""
        self.assertIsInstance(self.state, BaseModel)
