#!/usr/bin/python3
from models.base_model import BaseModel

class Place(BaseModel):
    """Place attributtes that inherits from basemodel"""

    def __init__(self, *args, **kwargs):
        self.city_id = ""
        self.name = ""
        self.number_of_rooms = 0
        self.number_of_bath = 0
        self.maximum_guest =0
        self.price = 0
        self.aminities = []
        self.latitutude = 0
        self.longitude = 0



