#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Unit tests for the City class"""

    def test_constructor(self):
        """Testing the constructor of the City class"""

        city = City()

        # Checking if the City instance is created
        self.assertIsInstance(city, City)

        # Checking if the 'name' and 'state_id' attributes are empty strings by default
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_attributes(self):
        """Testing setting attributes of the City class"""

        # Testing setting the 'name' and 'state_id' attributes
        city = City()
        city.name = "New York"
        city.state_id = "NY"
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.state_id, "NY")

    def test_to_dict(self):
        """Testing the to_dict() method of the City class"""

        city = City(name="New York", state_id="NY")
        city_dict = city.to_dict()

        # Checking if the returned dictionary has the correct keys and values
        self.assertIn("name", city_dict)
        self.assertEqual(city_dict["name"], "New York")
        self.assertIn("state_id", city_dict)
        self.assertEqual(city_dict["state_id"], "NY")
        self.assertIn("__class__", city_dict)
        self.assertEqual(city_dict["__class__"], "City")


if __name__ == "__main__":
    unittest.main()

