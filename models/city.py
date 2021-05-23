#!/usr/bin/python3
"""Module for class City. Inherits from BaseModel."""


from models.base_model import BaseModel
from datetime import datetime


class City(BaseModel):
    """City data - state_id and name of city"""

    state_id = ""
    name = ""
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
            City.count += 1
        else:
            super().__init__()
            City.count += 1
