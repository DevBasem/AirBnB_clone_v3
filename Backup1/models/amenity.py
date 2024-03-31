#!/usr/bin/python3
"""Module defining the Amenity class."""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Amenity class representing an amenity in the database.

    Attributes:
        __tablename__ (str): Name of the MySQL table for Amenity objects.
        name (sqlalchemy String): Name of the amenity.
        places (sqlalchemy relationship): Relationship with Place objects.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)
