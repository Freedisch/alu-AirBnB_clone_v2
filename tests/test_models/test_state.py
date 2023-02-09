#!/usr/bin/python3
"""unittest for User class"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for User subclass."""

    def setUp(self):
        self.testState = State()

    def test_State(self):
        """check if state class is subclass of BaseModel."""
        self.assertTrue(issubclass(self.testState.__class__, BaseModel))

    def test_name(self):
        """Test name is string attribute."""
        self.assertIsInstance(self.testState.name, str)


if __name__ == '__main__':
    unittest.main()
