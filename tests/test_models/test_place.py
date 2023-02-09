#!/usr/bin/python3
"""unittest for User class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for place sub class."""

    def setUp(self):
        self.testPlace = Place()

    def testPlace(self):
        """test if Place class is subclass of BaseModel."""
        self.assertTrue(issubclass(self.testPlace.__class__, BaseModel))

    def test_city_id(self):
        """test if city_id is a string attribute."""
        self.assertIsInstance(self.testPlace.city_id, str)

    def test_user_id(self):
        """test if user_id is a string attribute."""
        self.assertIsInstance(self.testPlace.user_id, str)

    def test_name(self):
        """test if name is a string attribute."""
        self.assertIsInstance(self.testPlace.name, str)

    def test_description(self):
        """test if description is a string attribute."""
        self.assertIsInstance(self.testPlace.description, str)

    def test_number_rooms(self):
        """test if number of rooms is an integer attribute."""
        self.assertIsInstance(self.testPlace.number_rooms, int)

    def test_number_bathrooms(self):
        """test if number of bathrooms is an integer attribute."""
        self.assertIsInstance(self.testPlace.number_bathrooms, int)

    def test_max_guest(self):
        """test if max_guests is an integer attribute."""
        self.assertIsInstance(self.testPlace.max_guest, int)

    def test_price_by_night(self):
        """test if price_by_night is an integer attribute."""
        self.assertIsInstance(self.testPlace.price_by_night, int)

    def test_latitude(self):
        """test if test_latitude is a float attribute."""
        self.assertIsInstance(self.testPlace.latitude, float)

    def test_longitude(self):
        """test if longitude is a float attribute."""
        self.assertIsInstance(self.testPlace.longitude, float)

    def test_amenity_ids(self):
        """test if amenity is a list attribute."""
        self.assertIsInstance(self.testPlace.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
