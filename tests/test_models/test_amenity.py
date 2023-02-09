#!/usr/bin/python3
"""unittest for User class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestState(unittest.TestCase):
    """Test cases for User subclass."""

    def setUp(self):
        self.testAmenity = Amenity()

    def test_Amenity(self):
        """check if Amenity class is subclass of BaseModel."""
        self.assertTrue(issubclass(self.testAmenity.__class__, BaseModel))

    def test_name(self):
        """Test whether name is string attribute."""
        self.assertIsInstance(self.testAmenity.name, str)


if __name__ == '__main__':
    unittest.main()
