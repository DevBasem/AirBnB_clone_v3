#!/usr/bin/python3
"""Module defining the City class."""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """City class representing a city in the database.

    Attributes:
        __tablename__ (str): Name of the MySQL table for City objects.
        name (sqlalchemy String): Name of the city.
        state_id (sqlalchemy String): ID of the state to which city.
        places (sqlalchemy relationship): Relationship to the Place model.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")

    def __str__(self):
        """String representation of the City object."""
        return "[City] ({}) {}".format(
            self.id,
            {
                'id': self.id,
                'updated_at': self.updated_at,
                'state_id': self.state_id,
                'name': self.name,
                'created_at': self.created_at
            }
        )
