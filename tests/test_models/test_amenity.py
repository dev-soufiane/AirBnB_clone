#!/usr/bin/python3
"""Unit tests for the Amenity class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

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
        """Test instantiation of Amenity class."""
        amenity_instance = Amenity()
        self.assertEqual(
                str(type(amenity_instance)),
                "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity_instance, Amenity)
        self.assertTrue(issubclass(type(amenity_instance), BaseModel))

    def test_8_attributes(self):
        """Test the attributes of Amenity class."""
        amenity_attributes = storage.attributes()["Amenity"]
        amenity_instance = Amenity()
        for attribute, attr_type in amenity_attributes.items():
            self.assertTrue(hasattr(amenity_instance, attribute))
            self.assertEqual(
                    type(getattr(amenity_instance, attribute, None)),
                    attr_type)


if __name__ == "__main__":
    unittest.main()
