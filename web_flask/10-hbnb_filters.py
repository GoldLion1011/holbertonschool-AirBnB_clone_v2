#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
import models
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(content):
    """ removes current SQLAlchemy sesh """
    models.storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """ displays HTML for cities w a State id """
    states = models.storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb-filters.html', state_list=states,
                           amnenity_list=amenities)
