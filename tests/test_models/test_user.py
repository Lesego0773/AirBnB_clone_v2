#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unit tests for the User class"""

    def test_constructor(self):
        """Testing the constructor of the User class"""

        user = User()

        # Checking if the User instance is created
        self.assertIsInstance(user, User)

        # Checking if the attributes are initialized correctly
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attributes(self):
        """Testing setting attributes of the User class"""

        # Testing setting the attributes
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        # Checking if the attributes are set correctly
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_to_dict(self):
        """Testing the to_dict() method of the User class"""

        user = User(email="test@example.com", password="password123", first_name="John", last_name="Doe")
        user_dict = user.to_dict()

        # Checking if the returned dictionary has the correct keys and values
        self.assertIn("email", user_dict)
        self.assertEqual(user_dict["email"], "test@example.com")
        self.assertIn("password", user_dict)
        self.assertEqual(user_dict["password"], "password123")
        self.assertIn("first_name", user_dict)
        self.assertEqual(user_dict["first_name"], "John")
        self.assertIn("last_name", user_dict)
        self.assertEqual(user_dict["last_name"], "Doe")


if __name__ == "__main__":
    unittest.main()

