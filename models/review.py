#!/usr/bin/python3
"""Module for class Review. Inherits from BaseModel"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Data that forms a review"""

    place_id = ""
    user_id = ""
    text = ""
