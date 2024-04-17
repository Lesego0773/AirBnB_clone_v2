#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Unit tests for the Review class"""

    def test_constructor(self):
        """Testing the constructor of the Review class"""

        review = Review()

        # Checking if the Review instance is created
        self.assertIsInstance(review, Review)

        # Checking if the attributes are initialized correctly
        self.assertEqual(review.place_identity, "")
        self.assertEqual(review.user_identity, "")
        self.assertEqual(review.text, "")

    def test_attributes(self):
        """Testing setting attributes of the Review class"""

        # Testing setting the attributes
        review = Review()
        review.place_identity = "123"
        review.user_identity = "456"
        review.text = "Great experience!"

        # Checking if the attributes are set correctly
        self.assertEqual(review.place_identity, "123")
        self.assertEqual(review.user_identity, "456")
        self.assertEqual(review.text, "Great experience!")

    def test_to_dict(self):
        """Testing the to_dict() method of the Review class"""

        review = Review(place_identity="123", user_identity="456", text="Great experience!")
        review_dict = review.to_dict()

        # Checking if the returned dictionary has the correct keys and values
        self.assertIn("place_identity", review_dict)
        self.assertEqual(review_dict["place_identity"], "123")
        self.assertIn("user_identity", review_dict)
        self.assertEqual(review_dict["user_identity"], "456")
        self.assertIn("text", review_dict)
        self.assertEqual(review_dict["text"], "Great experience!")


if __name__ == "__main__":
    unittest.main()

