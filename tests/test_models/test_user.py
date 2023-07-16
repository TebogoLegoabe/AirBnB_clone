#!/usr/bin/python3
"""import relevant modules"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """tests for the class User"""
    def setUp(self):
        """set up method"""
        self.user = User()

    def testClassPresent(self):
        """chck if class exists"""
        self.assertEqual(str(type(self.user)), "<class 'models.user.User'>")

    def testAttributesPresent(self):
        """check if attrs are present"""
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def testAttrTypes(self):
        """check for the right attr types"""
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def testIsInstance(self):
        """check if class is instance of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)
