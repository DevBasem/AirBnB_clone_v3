#!/usr/bin/python3
"""Module defining the User class."""

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User class representing a user in the database.

    Attributes:
        __tablename__ (str): Name of the MySQL table for User objects.
        email (sqlalchemy String): Email address of the user.
        password (sqlalchemy String): Password of the user.
        first_name (sqlalchemy String): First name of the user.
        last_name (sqlalchemy String): Last name of the user.
        places (sqlalchemy relationship): Relationship to the Place model.
        reviews (sqlalchemy relationship): Relationship to the Review model.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")

    def __str__(self):
        """String representation of the User object."""
        return "[User] ({}) {}".format(self.id, {
            'updated_at': self.updated_at,
            'id': self.id,
            'last_name': self.last_name,
            'first_name': self.first_name,
            'email': self.email,
            'created_at': self.created_at,
            'password': self.password
        })
