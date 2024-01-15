#!/usr/bin/python3
"""Unit tests for the City class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

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
        """Test instantiation of City class."""
        city_instance = City()
        self.assertEqual(
                str(type(city_instance)), "<class 'models.city.City'>")
        self.assertIsInstance(city_instance, City)
        self.assertTrue(issubclass(type(city_instance), BaseModel))

    def test_8_attributes(self):
        """Test the attributes of City class."""
        city_attributes = storage.attributes()["City"]
        city_instance = City()
        for attribute, attr_type in city_attributes.items():
            self.assertTrue(hasattr(city_instance, attribute))
            self.assertEqual(
                    type(getattr(city_instance, attribute, None)), attr_type)


if __name__ == "__main__":
    unittest.main()
