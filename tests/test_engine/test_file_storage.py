#!/usr/bin/python3
"""import modules"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """set up method"""
        self.file_instance = FileStorage()

    def test_all(self):
        """check that it returns a dict"""
        inst = self.file_instance.all()
        self.assertTrue(type(inst), dict)
