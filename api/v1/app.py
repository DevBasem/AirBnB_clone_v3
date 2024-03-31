#!/usr/bin/python3
""" config app """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv

host = getenv("HBNB_API_HOST", "0.0.0.0")
port = getenv("HBNB_API_PORT", "5000")

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage"""
    storage.close()


@app.errorhandler(404)
def page_not_found(exception):
    """ found 404 error """
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    app.run(host=host, port=port, threaded=True)
