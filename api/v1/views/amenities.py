#!/usr/bin/python3
""" Amenity API views """

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import abort, request, jsonify


@app_views.route("/amenities", strict_slashes=False, methods=["GET"])
@app_views.route("/amenities/<amenity_id>", strict_slashes=False,
                 methods=["GET"])
def amenity(amenity_id=None):
    """ Retrieves the list of all Amenity objects """
    all_list = []
    if amenity_id is None:
        all_obj = storage.all(Amenity).values()
        for value in all_obj:
            all_list.append(value.to_dict())
        return jsonify(all_list)
    else:
        results = storage.get(Amenity, amenity_id)
        if results is None:
            abort(404)
        return jsonify(results.to_dict())


@app_views.route("/amenities/<amenity_id>", strict_slashes=False,
                 methods=["DELETE"])
def amenity_delete(amenity_id):
    """delete method"""
    objects = storage.get(Amenity, amenity_id)
    if objects is None:
        abort(404)
    storage.delete(objects)
    storage.save()
    return jsonify({}), 200


@app_views.route("/amenities", strict_slashes=False, methods=["POST"])
def create_amenity():
    """create a new post req"""
    data = request.get_json(force=True, silent=True)
    if not data:
        abort(400, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")
    new_amenity = Amenity(**data)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route("/amenities/<amenity_id>", strict_slashes=False,
                 methods=["PUT"])
def update_amenity(amenity_id):
    """ Updates an Amenity object """
    objects = storage.get(Amenity, amenity_id)
    if objects is None:
        abort(404)
    data = request.get_json(force=True, silent=True)
    if not data:
        abort(400, "Not a JSON")
    objects.name = data.get("name", objects.name)
    objects.save()
    return jsonify(objects.to_dict()), 200
