#!/usr/bin/python3
"""
Contains tests for FileStorge class
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Tests for FileStorage class
    """

    def test_others(self):
        file_path = FileStorage._FileStorage__file_path
        if not os.path.exists(file_path):
            model = BaseModel()
            model.save()
        self.assertTrue(os.path.exists(file_path))

    def test_obj_dict(self):
        model = BaseModel()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
