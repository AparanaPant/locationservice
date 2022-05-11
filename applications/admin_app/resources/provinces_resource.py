from flask import request
from flask_restful import Resource

from core.extensions.database.mongodb_config import mongo
from core.serialize import serialize_many, serialize_one
from scripts.create_initial_database import insert_provinces, insert_cities, insert_areas


class ProvincesResource(Resource):
    def get(self):
        return serialize_many(mongo.db.provinces.find())

    def post(self):
        data = mongo.db.provinces.insert_one(request.json)
        return serialize_one(mongo.db.provinces.find_one(data.inserted_id))


class Test(Resource):
    def get(self):
        insert_provinces()
        insert_cities()
        insert_areas()
        return {}
