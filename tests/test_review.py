#!/usr/bin/python3
"""
Unittest for Review class
"""

import unittest
from models.review import Review
from datetime import datetime
import uuid
from unittest.mock import patch


class TestReview(unittest.TestCase):
    """
    Test cases for Review class
    """

    def test_init_no_kwargs(self):
        """
        Test initialization without kwargs
        """
        with patch('models.storage.new') as mock_storage_new:
            review = Review()
            self.assertIsInstance(review, Review)
            self.assertTrue(hasattr(review, "id"))
            self.assertTrue(hasattr(review, "created_at"))
            self.assertTrue(hasattr(review, "updated_at"))
            self.assertEqual(review.created_at, review.updated_at)
            self.assertEqual(review.place_id, "")
            self.assertEqual(review.user_id, "")
            self.assertEqual(review.text, "")
            mock_storage_new.assert_called_once_with(review)

    def test_init_with_kwargs(self):
        """
        Test initialization with kwargs
        """
        kwargs = {
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "place_id": "test_place_id",
            "user_id": "test_user_id",
            "text": "test_text"
        }
        review = Review(**kwargs)
        self.assertEqual(review.id, kwargs["id"])
        self.assertEqual(review.created_at,
                         datetime.fromisoformat(kwargs["created_at"]))
        self.assertEqual(review.updated_at,
                         datetime.fromisoformat(kwargs["updated_at"]))
        self.assertEqual(review.place_id, kwargs["place_id"])
        self.assertEqual(review.user_id, kwargs["user_id"])
        self.assertEqual(review.text, kwargs["text"])

    def test_str(self):
        """
        Test string representation
        """
        review = Review()
        class_name = review.__class__.__name__
        expected = f"[{class_name}] ({review.id}) {review.__dict__}"
        self.assertEqual(str(review), expected)

    def test_save(self):
        """
        Test save method for Review object
        """
        review = Review()
        old_updated_at = review.updated_at
        with patch('models.storage.save') as mock_storage_save:
            review.save()
            self.assertNotEqual(old_updated_at, review.updated_at)
            self.assertTrue(review.updated_at > old_updated_at)
            mock_storage_save.assert_called_once()

    def test_to_dict(self):
        """
        Test to_dict method for Review object
        """
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["id"], review.id)
        self.assertEqual(review_dict["created_at"],
                         review.created_at.isoformat())
        self.assertEqual(review_dict["updated_at"],
                         review.updated_at.isoformat())
        self.assertNotIn("place_id", review_dict)
        self.assertNotIn("user_id", review_dict)
        self.assertNotIn("text", review_dict)


if __name__ == "__main__":
    unittest.main()
