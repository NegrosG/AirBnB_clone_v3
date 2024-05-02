#!/usr/bin/python3
"""
create flask app, and register the blueprint app_views to flask instance app.
"""

from flask import Flask, jsonify
from os import getenv
from api.v1.views import app_views
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_engine(exception):
    """

    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """

    """
    resp = {"error": "Not found"}
    return jsonify(resp), 404


if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
