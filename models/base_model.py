#!/usr/bin/python3
# models/base_model.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid

Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())

    def save(self):
        from models.engine.db_storage import DBStorage  # Import here to avoid circular import
        self.updated_at = datetime.utcnow()
        storage = DBStorage()  # Initialize storage engine
        storage.new(self)
        storage.save()

    def delete(self):
        from models.engine.db_storage import DBStorage  # Import here to avoid circular import
        storage = DBStorage()  # Initialize storage engine
        storage.delete(self)

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

