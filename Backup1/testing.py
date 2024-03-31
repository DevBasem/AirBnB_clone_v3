#!/usr/bin/python3

from models.base_model import Base
from models.place import Place
from models.amenity import Amenity
from models.city import City  # Import City model
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

session = Session(engine)

# Create instances
city = City(id='some_city_id')  # Replace with the actual id
place = Place(name="Sample Place", city_id=city.id)
amenity = Amenity(name="Sample Amenity")

# Link them
place.amenities.append(amenity)
session.add_all([city, place, amenity])  # Add city, place, and amenity to the session

# No need to commit explicitly for in-memory SQLite
# The changes will be discarded when the session is closed

# Query and print
places = session.query(Place).all()
for p in places:
    print(p.amenities)
