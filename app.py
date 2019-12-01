from os import environ

from bson import json_util
from bson.objectid import ObjectId
from flask import Flask, jsonify
from flask_pymongo import PyMongo

from src.mongoflask  import MongoJSONEncoder, ObjectIdConverter, find_restaurants

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongodb:mongodb@127.0.0.1:27017/intelygenz"
app.json_encoder = MongoJSONEncoder
app.url_map.converters["objectid"] = ObjectIdConverter
mongo = PyMongo(app)


@app.route("/api/v1/restaurant")
def restaurants():
    restaurants = find_restaurants(mongo)
    return jsonify(restaurants)


@app.route("/api/v1/restaurant/<id>")
def restaurant(id):
    restaurants = find_restaurants(mongo, id)
    if not restaurants:
        return jsonify(restaurants), 204
    else:
        return jsonify(restaurants[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=8080)
