#!/usr/bin/python3
"""unittest for User class"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for User subclass."""

    def setUp(self):
        self.testCity = City()

    def test_City(self):
        """check if city class is subclass of BaseModel."""
        self.assertTrue(issubclass(self.testCity.__class__, BaseModel))

    def test_state_id(self):
        """Test city.state_id is str attribute."""
        self.assertIsInstance(self.testCity.state_id, str)

    def test_City(self):
        """test whether name in city is a string attribute"""

        self.assertIsInstance(self.testCity.name, str)


if __name__ == '__main__':
    unittest.main()
