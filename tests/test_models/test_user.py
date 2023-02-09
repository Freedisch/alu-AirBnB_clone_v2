# #!/usr/bin/python3
# """unittest for User class"""
# import unittest
# from models.base_model import BaseModel
# from models.user import User


# class TestUser(unittest.TestCase):
#     """Test cases for User subclass."""

#     def setUp(self):
#         self.testUser = User()

#     def test_user(self):
#         """check if User class is subclass of BaseModel."""
#         self.assertTrue(issubclass(self.testUser.__class__, BaseModel))

#     def test_email(self):
#         """Test email class attribute."""
#         self.assertIsInstance(self.testUser.email, str)

#     def test_password(self):
#         """ check whether password is a string instance"""
#         self.assertIsInstance(self.testUser.password, str)

#     def test_first_name(self):
#         """ check whether first_name is a string instance"""
#         self.assertIsInstance(self.testUser.first_name, str)

#     def test_last_name(self):
#         """ check whether last_name is a string instance"""
#         self.assertIsInstance(self.testUser.last_name, str)


# if __name__ == '__main__':
#     unittest.main()
