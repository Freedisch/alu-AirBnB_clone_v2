
from models import base_model
from datetime import datetime
import unittest

class TestBaseModel(unittest.TestCase):
    def test__init(self):
        # check whether id, created_at, updated_at have been set correctly
        x = base_model.BaseModel()
        self.assertIsInstance(x.id, str)
        self.assertIsInstance(x.created_at, str)
        self.assertIsInstance(x.updated_at, str)

