#!/usr/bin/python3
import json
import datetime as dt
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),

        }

    def from_dict(self, data):
        self.id = data['id']
        self.created_at = dt.datetime.strptime(data['created_at'], '%Y-%m-%dT%H:%M:%S.%f')


    def to_json(self):
        return json.dumps(self.to_dict())

    def from_json(self, json_str):
        data = json.loads(json_str)
        self.from_dict(data)









