#!/usr/bin/python3
"""Defines the State class."""
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(models.City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

    # Add a custom __str__ method
    def __str__(self):
        """Return a string representation of the State object."""
        return "[State] ({}) {}".format(
            self.id,
            {
                'name': self.name,
                'id': self.id,
                'updated_at': self.updated_at,
                'created_at': self.created_at
            }
        )
