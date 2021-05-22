#!/usr/bin/python3
"""Module for unit tests for class Review"""

import unittest
from models.review import Review

r = Review()


class test_review(unittest.TestCase):
    """Holds tests for class Review"""

    def test_place_id(self):
        self.assertTrue(hasattr(r, "place_id"))
        self.assertIsInstance(r.place_id, str)

    def test_usr_id(self):
        self.assertTrue(hasattr(r, "usr_id"))
        self.assertIsInstance(r.state_id, str)

    def text(self):
        self.assertTrue(hasattr(r, "text"))
        self.assertIsInstance(r.text, str)

if __name__ == '__main__':
        unittest.main()
