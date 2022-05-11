from bson import ObjectId
from bson.errors import InvalidId
from flask import request
from flask_restful import Resource

from core.exceptions.exception_baseclass import EntityDoesntExistError
from core.extensions.database.mongodb_config import mongo
from core.serialize import serialize_one


# from core.utils.db_utils import find_by_id_or_404

class ProvinceResource(Resource):
    def get(self, province_id):
        try:
            return serialize_one(mongo.db.provinces.find_one_or_404({"_id": ObjectId(province_id)}))
        except InvalidId as e:
            raise EntityDoesntExistError()

    def put(self, province_id):
        query = {"_id": ObjectId(province_id)}
        province = mongo.db.provinces.update_one(query, {"$set": request.json})
        return serialize_one(mongo.db.provinces.find_one(province.upserted_id))

    def patch(self, province_id):
        query = {"_id": ObjectId(province_id)}
        province = mongo.db.provinces.update_one(query, {"$set": request.json})
        return serialize_one(mongo.db.provinces.find_one(province.upserted_id))
