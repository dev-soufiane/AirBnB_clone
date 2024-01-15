#!/usr/bin/python3
"""State Module"""
from models.base_model import BaseModel


class State(BaseModel):
    """State Class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize State"""
        super().__init__(*args, **kwargs)
