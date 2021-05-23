#!/usr/bin/python3
"""Unit test cases for class Amenity(inherits from BaseModel)"""

import unittest
from models.amenity import Amenity

a = Amenity()


class test_amenity(unittest.TestCase):
    """Holds tests for class State"""

    def test_name(self):
        self.assertTrue(hasattr(a, "name"))
        self.assertIsInstance(a.name, str)

if __name__ == '__main__':
        unittest.main()
