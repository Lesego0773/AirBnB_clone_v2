#!/usr/bin/python3
from sqlalchemy import Table, Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

# Defining the association table for the many-to-many relationship
place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
)

class Place(BaseModel, Base):
    __tablename__ = 'places'

    id = Column(String(60), primary_key=True)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    # Defining the relationship with Amenity
    if storage_type == 'db':
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)


