#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up test methods."""
        pass

    def tearDown(self):
        """Tear down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset FileStorage data."""
        storage._FileStorage__objects = {}
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)

    def test_instantiation(self):
        """Test instantiation of User class."""
        user_instance = User()
        self.assertEqual(str(type(user_instance)), "<class 'models.user.User'>")
        self.assertIsInstance(user_instance, User)
        self.assertTrue(issubclass(type(user_instance), BaseModel))

    def test_attributes(self):
        """Test the attributes of User class."""
        user_attributes = storage.attributes()["User"]
        user_instance = User()
        for attribute, data_type in user_attributes.items():
            self.assertTrue(hasattr(user_instance, attribute))
            self.assertEqual(type(getattr(user_instance, attribute, None)), data_type)


if __name__ == "__main__":
    unittest.main()
