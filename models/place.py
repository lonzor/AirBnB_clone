#!/usr/bin/python3
"""Module for class Place. Inherits from BaseModel"""


from models.base_model import BaseModel
from datetime import datetime


class Place(BaseModel):
    """Has lots of data about the Airbnb listing"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
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
            Place.count += 1
        else:
            super().__init__()
            Place.count += 1
