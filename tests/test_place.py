#!/usr/bin/python3
"""
Unittest for Place class
"""

import unittest
from models.place import Place
from datetime import datetime
import uuid
from unittest.mock import patch


class TestPlace(unittest.TestCase):
    """
    Test cases for Place class
    """

    def test_init_no_kwargs(self):
        """
        Test initialization without kwargs
        """
        with patch('models.storage.new') as mock_storage_new:
            place = Place()
            self.assertIsInstance(place, Place)
            self.assertTrue(hasattr(place, "id"))
            self.assertTrue(hasattr(place, "created_at"))
            self.assertTrue(hasattr(place, "updated_at"))
            self.assertEqual(place.created_at, place.updated_at)
            self.assertEqual(place.city_id, "")
            self.assertEqual(place.user_id, "")
            self.assertEqual(place.name, "")
            self.assertEqual(place.description, "")
            self.assertEqual(place.number_rooms, 0)
            self.assertEqual(place.number_bathrooms, 0)
            self.assertEqual(place.max_guest, 0)
            self.assertEqual(place.price_by_night, 0)
            self.assertEqual(place.latitude, 0.0)
            self.assertEqual(place.longitude, 0.0)
            self.assertEqual(place.amenity_ids, [])
            mock_storage_new.assert_called_once_with(place)

    def test_init_with_kwargs(self):
        """
        Test initialization with kwargs
        """
        kwargs = {
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "city_id": "test_city_id",
            "user_id": "test_user_id",
            "name": "test_name",
            "description": "test_description",
            "number_rooms": 3,
            "number_bathrooms": 2,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 12.34,
            "longitude": 56.78,
            "amenity_ids": ["test_amenity"]
        }
        place = Place(**kwargs)
        self.assertEqual(place.id, kwargs["id"])
        self.assertEqual(place.created_at,
                         datetime.fromisoformat(kwargs["created_at"]))
        self.assertEqual(place.updated_at,
                         datetime.fromisoformat(kwargs["updated_at"]))
        self.assertEqual(place.city_id, kwargs["city_id"])
        self.assertEqual(place.user_id, kwargs["user_id"])
        self.assertEqual(place.name, kwargs["name"])
        self.assertEqual(place.description, kwargs["description"])
        self.assertEqual(place.number_rooms, kwargs["number_rooms"])
        self.assertEqual(place.number_bathrooms, kwargs["number_bathrooms"])
        self.assertEqual(place.max_guest, kwargs["max_guest"])
        self.assertEqual(place.price_by_night, kwargs["price_by_night"])
        self.assertEqual(place.latitude, kwargs["latitude"])
        self.assertEqual(place.longitude, kwargs["longitude"])
        self.assertEqual(place.amenity_ids, kwargs["amenity_ids"])

    def test_str(self):
        """
        Test string representation of Place object
        """
        place = Place()
        class_name = place.__class__.__name__
        expected = f"[{class_name}] ({place.id}) {place.__dict__}"
        self.assertEqual(str(place), expected)

    def test_save(self):
        """
        Test save method for Place object
        """
        place = Place()
        old_updated_at = place.updated_at
        with patch('models.storage.save') as mock_storage_save:
            place.save()
            self.assertNotEqual(old_updated_at, place.updated_at)
            self.assertTrue(place.updated_at > old_updated_at)
            mock_storage_save.assert_called_once()

    def test_to_dict(self):
        """
        Test to_dict method for Place object
        """
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["id"], place.id)
        self.assertEqual(place_dict["created_at"],
                         place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"],
                         place.updated_at.isoformat())
        self.assertNotIn("city_id", place_dict)
        self.assertNotIn("user_id", place_dict)
        self.assertNotIn("name", place_dict)
        self.assertNotIn("description", place_dict)
        self.assertNotIn("number_rooms", place_dict)
        self.assertNotIn("number_bathrooms", place_dict)
        self.assertNotIn("max_guest", place_dict)
        self.assertNotIn("price_by_night", place_dict)
        self.assertNotIn("latitude", place_dict)
        self.assertNotIn("longitude", place_dict)
        self.assertNotIn("amenity_ids", place_dict)


if __name__ == "__main__":
    unittest.main()
