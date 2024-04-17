#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unit tests for the Place class"""

    def test_constructor(self):
        """Testing the constructor of the Place class"""

        place = Place()

        # Checking if the Place instance is created
        self.assertIsInstance(place, Place)

        # Checking if the attributes are initialized correctly
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.number_of_rooms, 0)
        self.assertEqual(place.number_of_bath, 0)
        self.assertEqual(place.maximum_guest, 0)
        self.assertEqual(place.price, 0)
        self.assertEqual(place.amenities, [])
        self.assertEqual(place.latitude, 0)
        self.assertEqual(place.longitude, 0)

    def test_attributes(self):
        """Test setting attributes of the Place class"""

        # Testing setting the attributes
        place = Place()
        place.city_id = "123"
        place.name = "Cozy Cabin"
        place.number_of_rooms = 2
        place.number_of_bath = 1
        place.maximum_guest = 4
        place.price = 100
        place.amenities = ["WiFi", "Kitchen"]
        place.latitude = 40.7128
        place.longitude = -74.0060

        # Checking if the attributes are set correctly
        self.assertEqual(place.city_id, "123")
        self.assertEqual(place.name, "Cozy Cabin")
        self.assertEqual(place.number_of_rooms, 2)
        self.assertEqual(place.number_of_bath, 1)
        self.assertEqual(place.maximum_guest, 4)
        self.assertEqual(place.price, 100)
        self.assertEqual(place.amenities, ["WiFi", "Kitchen"])
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)

    def test_to_dict(self):
        """Testing the to_dict() method of the Place class"""

        place = Place(
            city_id="123",
            name="Cozy Cabin",
            number_of_rooms=2,
            number_of_bath=1,
            maximum_guest=4,
            price=100,
            amenities=["WiFi", "Kitchen"],
            latitude=40.7128,
            longitude=-74.0060
        )
        place_dict = place.to_dict()

        # Checking if the returned dictionary has the correct keys and values
        self.assertIn("city_id", place_dict)
        self.assertEqual(place_dict["city_id"], "123")
        self.assertIn("name", place_dict)
        self.assertEqual(place_dict["name"], "Cozy Cabin")
        self.assertIn("number_of_rooms", place_dict)
        self.assertEqual(place_dict["number_of_rooms"], 2)
        self.assertIn("number_of_bath", place_dict)
        self.assertEqual(place_dict["number_of_bath"], 1)
        self.assertIn("maximum_guest", place_dict)
        self.assertEqual(place_dict["maximum_guest"], 4)
        self.assertIn("price", place_dict)
        self.assertEqual(place_dict["price"], 100)
        self.assertIn("amenities", place_dict)
        self.assertEqual(place_dict["amenities"], ["WiFi", "Kitchen"])
        self.assertIn("latitude", place_dict)
        self.assertEqual(place_dict["latitude"], 40.7128)
        self.assertIn("longitude", place_dict)
        self.assertEqual(place_dict["longitude"], -74.0060)


if __name__ == "__main__":
    unittest.main()

