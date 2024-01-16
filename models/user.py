#!/usr/bin/python3
"""Module for the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines the User class."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
