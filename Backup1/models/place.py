#!/usr/bin/python3
"""Module defining the Place class."""

import models
from models.amenity import Amenity
import os
from os import getenv
from models.base_model import Base, BaseModel
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

# Define the association table for the many-to-many relationship
place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """Place class representing a place in the database.

    Attributes:
        __tablename__ (str): Name of the MySQL table for Place objects.
        city_id (sqlalchemy String): City id where the place is located.
        user_id (sqlalchemy String): User id of the place's owner.
        name (sqlalchemy String): Name of the place.
        description (sqlalchemy String): Description of the place.
        number_rooms (sqlalchemy Integer): Number of rooms in the place.
        number_bathrooms (sqlalchemy Integer): Number of bathrooms in the place.
        max_guest (sqlalchemy Integer): Maximum number of guests in the place.
        price_by_night (sqlalchemy Integer): Price per night for the place.
        latitude (sqlalchemy Float): Latitude of the place.
        longitude (sqlalchemy Float): Longitude of the place.
        reviews (sqlalchemy relationship): Relationship to the Review model.
        amenities (sqlalchemy relationship): Relationship to the Amenity model.
        amenity_ids (list): List of linked amenity ids.
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get a list of all linked Reviews."""
            review_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Get/set linked Amenities."""
            amenity_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)

    def __str__(self):
        """
        Returns a string representation of the Place object

        Returns:
            str: String representation of the object
        """
        custom_attrs = {
            'latitude': self.latitude,
            'city_id': self.city_id,
            'price_by_night': self.price_by_night,
            'id': self.id,
            'user_id': self.user_id,
            'max_guest': self.max_guest,
            'created_at': self.created_at,
            'description': self.description,
            'number_rooms': self.number_rooms,
            'longitude': self.longitude,
            'number_bathrooms': self.number_bathrooms,
            'name': self.name,
            'updated_at': self.updated_at
        }

        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            custom_attrs
        )
