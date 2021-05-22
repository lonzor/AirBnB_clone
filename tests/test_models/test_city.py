#!/usr/bin/python3
"""Unit test cases for class City(inherits from BaseModel)"""

import unittest
from models.city import City

c = City()


class test_city(unittest.TestCase):
    """Holds tests for class State"""

    def test_name(self):
        self.assertTrue(hasattr(c, "name"))
        self.assertIsInstance(c.name, str)

    def test_state_id(self):
        self.assertTrue(hasattr(c, "state_id"))
        self.assertIsInstance(c.state_id, str)

if __name__ == '__main__':
        unittest.main()
