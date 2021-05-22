#!/usr/bin/python3
"""Unit test cases for class State(inherits from BaseModel)"""

import unittest
from models.state import State


class test_state(unittest.TestCase):
    """Holds tests for class State"""

    def test_name(self):
        st = State()
        self.assertTrue(hasattr(st, "name"))
        self.assertIsInstance(st.name, str)

if __name__ == '__main__':
        unittest.main()
