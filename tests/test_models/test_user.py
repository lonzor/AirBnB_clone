#!/usr/bin/python3
"""
This module contains unittests for the User class
"""
import unittest
import os
from models.user import User


u = User()


class TestUser(unittest.TestCase):
    """Unittests for User class"""

    def test_email(self):
        self.assertTrue(hasattr(u, "email"))
        self.assertIsInstance(u.email, str)
        
    def test_password(self):
        self.assertTrue(hasattr(u, "password"))
        self.assertIsInstance(u.password, str)
        
    def test_first_name(self):
        self.assertTrue(hasattr(u, "first_name"))
        self.assertIsInstance(u.first_name, str)
        
    def test_last_name(self):
        self.assertTrue(hasattr(u, "last_name"))
        self.assertIsInstance(u.last_name, str)

if __name__ == '__main__':
        unittest.main()
