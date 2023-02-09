# #!/usr/bin/python3
# """unittest for User class"""
# import unittest
# from models.base_model import BaseModel
# from models.review import Review


# class TestReview(unittest.TestCase):
#     """Test cases for Review subclass."""

#     def setUp(self):
#         self.testReview = Review()

#     def test_Review(self):
#         """check if Review class is subclass of BaseModel."""
#         self.assertTrue(issubclass(self.testReview.__class__, BaseModel))

#     def test_Place_id(self):
#         """Test review.place_id is str attribute."""
#         self.assertIsInstance(self.testReview.place_id, str)

#     def test_user_id(self):
#         """test whether state_id in Review is a string attribute"""

#         self.assertIsInstance(self.testReview.user_id, str)

#     def test_text(self):
#         """test whether the text in Review is a string attribute"""
#         self.assertIsInstance(self.testReview.text, str)


# if __name__ == '__main__':
#     unittest.main()
