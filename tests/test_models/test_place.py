#!/usr/bin/python3
"""Unit tests for place."""

import unittest
from models.place import Place


p = Place()


class test_place(unittest.TestCase):
    """Tests for place"""
    def test_city_id(self):
        self.assertTrue(hasattr(p, "city_id"))
        self.assertIsInstance(p.city_id, str)

    def test_user_id(self):
        self.assertTrue(hasattr(p, "user_id"))
        self.assertIsInstance(p.user_id, str)

    def test_name(self):
        self.assertTrue(hasattr(p, "name"))
        self.assertIsInstance(p.name, str)

    def test_description(self):
        self.assertTrue(hasattr(p, "description"))
        self.assertIsInstance(p.description, str)

    def test_number_rooms(self):
        self.assertTrue(hasattr(p, "number_rooms"))
        self.assertIsInstance(p.number_rooms, int)

    def test_number_bathrooms(self):
        self.assertTrue(hasattr(p, "number_bathrooms"))
        self.assertIsInstance(p.number_bathrooms, int)

    def test_max_guest(self):
        self.assertTrue(hasattr(p, "max_guest"))
        self.assertIsInstance(p.max_guest, int)

    def test_price_by_night(self):
        self.assertTrue(hasattr(p, "price_by_night"))
        self.assertIsInstance(p.price_by_night, int)

    def test_latitude(self):
        self.assertTrue(hasattr(p, "latitude"))
        self.assertIsInstance(p.latitude, float)

    def test_longitude(self):
        self.assertTrue(hasattr(p, "longitude"))
        self.assertIsInstance(p.longitude, float)

    def test_amenity_ids(self):
        self.assertTrue(hasattr(p, "amenity_ids"))
        self.assertIsInstance(p.amenity_ids, list)

if __name__ == '__main__':
        unittest.main()
