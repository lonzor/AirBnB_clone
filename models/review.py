#!/usr/bin/python3
"""Module for class Review. Inherits from BaseModel"""

from models.base_model import BaseModel
from datetime import datetime


class Review(BaseModel):
    """Data that forms a review"""

    place_id = ""
    user_id = ""
    text = ""
    count = 0

    def __init__(self, *args, **kwargs):
        """
        Constructor of class User instance
        """
        if kwargs is not None and len(kwargs) != 0:
            for i in kwargs:
                if i == "__class__":
                    continue
                if i == "created_at" or i == "updated_at":
                    kwargs[i] = datetime.strptime(kwargs[i],
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, i, kwargs[i])
            Review.count += 1
        else:
            super().__init__()
            Review.count += 1
