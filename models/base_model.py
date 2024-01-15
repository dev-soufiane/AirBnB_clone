#!/usr/bin/python3
"""Defines BaseModel with common attributes/methods for other classes."""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines common attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        """Initializes instance attributes."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Returns instance as a string."""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        data = self.__dict__.copy()
        data['__class__'] = type(self).__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
