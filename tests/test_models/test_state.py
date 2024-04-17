#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Unit tests for the State class"""

    def test_constructor(self):
        """Testing the constructor of the State class"""

        state = State()

        # Checking if the State instance is created
        self.assertIsInstance(state, State)

        # Checking if the 'name' attribute is an empty string by default
        self.assertEqual(state.name, "")

    def test_attributes(self):
        """Testing setting attributes of the State class"""

        # Testing setting the 'name' attribute
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_to_dict(self):
        """Testing the to_dict() method of the State class"""

        state = State(name="California")
        state_dict = state.to_dict()

        # Checking if the returned dictionary has the correct keys and values
        self.assertIn("name", state_dict)
        self.assertEqual(state_dict["name"], "California")
        self.assertIn("__class__", state_dict)
        self.assertEqual(state_dict["__class__"], "State")


if __name__ == "__main__":
    unittest.main()

