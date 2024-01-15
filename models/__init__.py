#!/usr/bin/python3
"""This script initializes the package models"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
