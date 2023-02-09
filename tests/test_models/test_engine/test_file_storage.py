from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    def test__init(self):
        # check whether id, created_at, updated_at have been set correctly
        x = BaseModel()
        self.assertIsInstance(x.id, str)
        self.assertIsInstance(x.created_at, datetime)
        self.assertIsInstance(x.updated_at, datetime)
