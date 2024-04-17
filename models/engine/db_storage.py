#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    __engine = None
    __session_maker = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        self.__session_maker = scoped_session(sessionmaker(bind=self.__engine))

    def all(self, cls=None):
        session = self.__session_maker()
        objects = {}
        if cls:
            objects = session.query(cls).all()
        else:
            for cl in [User, State, City, Amenity, Place, Review]:
                objects += session.query(cl).all()
        session.close()
        return objects

    def new(self, obj):
        session = self.__session_maker()
        session.add(obj)
        session.commit()
        session.close()

    def save(self):
        session = self.__session_maker()
        session.commit()
        session.close()

    def delete(self, obj=None):
        if obj:
            session = self.__session_maker()
            session.delete(obj)
            session.commit()
            session.close()

