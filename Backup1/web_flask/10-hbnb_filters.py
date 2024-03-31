#!/usr/bin/python3
""" Starts a flask web application """
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def dispose(exception):
    """ Exit SQLAlchemy session """
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=list(states.values()),
                           amenities=list(amenities.values()))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
