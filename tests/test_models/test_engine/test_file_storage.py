#!/usr/bin/python3
"""
Contains tests for FileStorge class
"""
import unittest
import os
import json
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
        self.assertTrue(os.path.exists(file_path))
        fs = FileStorage()
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        model = BaseModel()
        model.save()
        self.assertNotEqual(os.path.getsize(fs._FileStorage__file_path), 0)

    def test_obj_dict(self):
        model = BaseModel()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
