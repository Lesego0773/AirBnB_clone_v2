#!/usr/bin/python3
import unittest

from models.amenity import Amenity




class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class"""

    def test_constructor(self):
        """Test the constructor of the Amenity class"""

        amenity = Amenity()

        # Checking if the Amenity instance is created
        self.assertIsInstance(amenity, Amenity)

        # Checking if the 'name' attribute is an empty string by default
        self.assertEqual(amenity.name, "")

    def test_attributes(self):
        """Test setting attributes of the Amenity class"""

        # Testing setting the 'name' attribute
        amenity = Amenity()
        amenity.name = "WiFi"
        self.assertEqual(amenity.name, "WiFi")

    def test_to_dict(self):
        """Testing the to_dict() method of the Amenity class"""

        amenity = Amenity(name="WiFi")
        amenity_dict = amenity.to_dict()

        # Checking if the returned dictionary has the correct keys and values
        self.assertIn("name", amenity_dict)
        self.assertEqual(amenity_dict["name"], "WiFi")
        self.assertIn("__class__", amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")


if __name__ == "__main__":
    unittest.main()

