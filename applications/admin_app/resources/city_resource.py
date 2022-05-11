from bson import ObjectId
from bson.errors import InvalidId
from flask import request
from flask_restful import Resource

from core.exceptions.exception_baseclass import EntityDoesntExistError
from core.extensions.database.mongodb_config import mongo
from core.serialize import serialize_one


class CityResource(Resource):
    def get(self, city_id):
        try:
            return serialize_one(mongo.db.cities.find_one_or_404({"_id": ObjectId(city_id)}))
        except InvalidId as e:
            raise EntityDoesntExistError()

    def put(self, city_id):
        query = {"_id": ObjectId(city_id)}
        city = mongo.db.cities.update_one(query, {"$set": request.json})
        return serialize_one(mongo.db.cities.find_one(city.upserted_id))

    # todo:only allow disable:true keyword for patch
    def patch(self, city_id):
        query = {"_id": ObjectId(city_id)}
        city = mongo.db.cities.update_one(query, {"$set": request.json})
        return serialize_one(mongo.db.cities.find_one(city.upserted_id))
