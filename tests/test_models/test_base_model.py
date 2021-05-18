#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import os
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Tests BaseModel class
    """

    def test_save(self):
        model = BaseModel()
        time1 = model.updated_at
        model.save()
        time2 = model.updated_at
        self.assertNotEqual(time1, time2)

    def test_to_dict(self):
        model = BaseModel()
        dict1 = model.to_dict()
        self.assertIn("__class__", dict1.keys())

    def test_self_id(self):
        model = BaseModel()
        self.assertNotEqual(model.id, "")

    def test_created_at(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_str(self):
        model = BaseModel()
        self.assertIn(model.id, model.__str__())
        self.assertIn(str(model.__dict__), model.__str__())
