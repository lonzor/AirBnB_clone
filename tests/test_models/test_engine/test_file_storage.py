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
        file_path = "file.json"
        if not os.path.exists(file_path):
            model = BaseModel()
        self.assertTrue(os.path.exists(file_path))
        if os.path.exists(file_path):
            os.remove(file_path)
        model = BaseModel()
        model.save()
        with open(file_path, "r") as f:
            original = f.read()
        model.save()
        with open(file_path, "r") as f:
            new = f.read()
        self.assertNotEqual(original, new)

    def test_obj_dict(self):
        model = BaseModel()
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
