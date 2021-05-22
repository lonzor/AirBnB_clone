#!/usr/bin/python3
"""
This module contains unittests for the User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for User class"""
    def test_user(self):
        u = User()
        u.email = "hello@goodbye.com"
        self.assertTrue(hasattr(u, "email"))
        u.password = "password"
        self.assertTrue(hasattr(u, "password"))
        u.first_name = "Betty"
        self.assertTrue(hasattr(u, "first_name"))
        u.last_name = "Holberton"
        self.assertTrue(hasattr(u, "last_name"))
