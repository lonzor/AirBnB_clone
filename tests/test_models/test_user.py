#!/usr/bin/python3
"""
This module contains unittests for the User class
"""
import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for User class"""

    def test_user(self):
        file_path = "file.json"
        if os.path.exists(file_path):
            os.remove(file_path)
        u = User()
        u.email = "hello@goodbye.com"
        self.assertTrue(hasattr(u, "email"))
        self.assertIsInstance(u.email, str)
        u.password = "password"
        self.assertTrue(hasattr(u, "password"))
        self.assertIsInstance(u.password, str)
        u.first_name = "Betty"
        self.assertTrue(hasattr(u, "first_name"))
        self.assertIsInstance(u.first_name, str)
        u.last_name = "Holberton"
        self.assertTrue(hasattr(u, "last_name"))
        self.assertIsInstance(u.last_name, str)

if __name__ == '__main__':
        unittest.main()
