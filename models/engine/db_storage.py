#!/usr/bin/python3

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        os.environ['HBNB_MYSQL_USER'] = 'your_mysql_user'
        os.environ['HBNB_MYSQL_PWD'] = 'your_mysql_password'
        os.environ['HBNB_MYSQL_HOST'] = 'your_mysql_host'
        os.environ['HBNB_MYSQL_DB'] = 'your_mysql_database'

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(os.getenv('HBNB_MYSQL_USER'),
                                             os.getenv('HBNB_MYSQL_PWD'),
                                             os.getenv('HBNB_MYSQL_HOST'),
                                             os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        session = self.__session()
        objects = {}
        if cls:
            objects = session.query(cls).all()
        else:
            for cl in [User, State, City, Amenity, Place, Review]:
                objects += session.query(cl).all()
        session.close()
        return objects

    def new(self, obj):
        session = self.__session()
        session.add(obj)
        session.commit()
        session.close()

    def save(self):
        session = self.__session()
        session.commit()
        session.close()

    def delete(self, obj=None):
        if obj:
            session = self.__session()
            session.delete(obj)
            session.commit()
            session.close()


