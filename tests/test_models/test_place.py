#!/usr/bin/python3
"""Unit tests for the Place class."""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

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
        """Test instantiation of Place class."""
        place_instance = Place()
        self.assertEqual(
                str(type(place_instance)), "<class 'models.place.Place'>")
        self.assertIsInstance(place_instance, Place)
        self.assertTrue(issubclass(type(place_instance), BaseModel))

    def test_8_attributes(self):
        """Test the attributes of Place class."""
        place_attributes = storage.attributes()["Place"]
        place_instance = Place()
        for attribute, attr_type in place_attributes.items():
            self.assertTrue(hasattr(place_instance, attribute))
            self.assertEqual(
                    type(getattr(place_instance, attribute, None)), attr_type)


if __name__ == "__main__":
    unittest.main()
