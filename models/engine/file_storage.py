#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    def __init__(self, filename="file.json"):
        self.filename = filename
        self.__objects = {}

    def all(self, cls=None):
        if cls is None:
            return self.__objects
        else:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.filename, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    cls = eval(class_name)
                    obj = cls(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects.pop(key, None)



