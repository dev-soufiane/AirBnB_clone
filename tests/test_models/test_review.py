#!/usr/bin/python3
"""Unit tests for the Review class."""

import unittest
from datetime import datetime
import time
from models.review import Review
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        """Set up test methods."""
        pass

    def tearDown(self):
        """Tear down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Test instantiation of Review class."""
        review_instance = Review()
        self.assertEqual(
                str(type(review_instance)), "<class 'models.review.Review'>")
        self.assertIsInstance(review_instance, Review)
        self.assertTrue(issubclass(type(review_instance), BaseModel))

    def test_8_attributes(self):
        """Test the attributes of Review class."""
        review_attributes = storage.attributes()["Review"]
        review_instance = Review()
        for attribute, attr_type in review_attributes.items():
            self.assertTrue(hasattr(review_instance, attribute))
            self.assertEqual(
                    type(getattr(review_instance, attribute, None)), attr_type)


if __name__ == "__main__":
    unittest.main()
