#!/usr/bin/python3
from models.base_model import BaseModel

class City(BaseModel):
    """City class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name = ""
        self.state_id = ""
