#!/usr/bin/python3
"""
Contains tests for FileStorge class
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


fs = FileStorage()


class TestFileStorage(unittest.TestCase):
    """
    Tests for FileStorage class
    """
    model = BaseModel()
    file_path = fs._FileStorage__file_path

    def test_all(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.assertIsInstance(fs.all(), dict)

    def test_new(self):
        fs_all = fs.all().copy()
        model2 = BaseModel()
        self.assertNotEqual(fs_all, fs.all())

    def test_save(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        model2 = BaseModel()
        model2.save()
        self.assertNotEqual(os.path.getsize(self.file_path), 0)

    def test_reload(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        model2 = BaseModel()
        model2.save()
        fs.reload()
        all_dict = fs.all().copy()
        model2.my_num = 100
        self.assertEqual(model2.my_num, 100)
        fs.reload()
        self.assertNotEqual(fs.all(), all_dict)

    def test_obj_dict(self):
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

if __name__ == '__main__':
        unittest.main()
