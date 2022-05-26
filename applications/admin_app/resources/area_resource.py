from bson import ObjectId
from bson.errors import InvalidId
from flask import request
from flask_restful import Resource

from core.exceptions.exception_baseclass import EntityDoesntExistError
from core.extensions.database.mongodb_config import mongo
from core.serialize import serialize_one


class AreaResource(Resource):
    def get(self, area_id):
        try:
            return serialize_one(mongo.db.areas.find_one({"_id": ObjectId(area_id)}))
        except InvalidId as e:
            raise EntityDoesntExistError()

    def put(self, area_id):
        query = {"_id": ObjectId(area_id)}
        area = mongo.db.cities.update_one(query, {"$set": request.json})
        return serialize_one(mongo.db.areas.find_one(area.upserted_id))

    # todo:only allow disable:true keyword for patch
    def patch(self, area_id):
        query = {"_id": ObjectId(area_id)}
        area = mongo.db.areas.update_one(query, {"$set": request.json})
        return serialize_one(mongo.db.areas.find_one(area.upserted_id))

