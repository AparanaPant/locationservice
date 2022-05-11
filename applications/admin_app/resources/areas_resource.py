from bson import ObjectId
from bson.errors import InvalidId
from flask import request
from flask_restful import Resource

from core.exceptions.exception_baseclass import BadRequest
from core.extensions.database.mongodb_config import mongo
from core.serialize import serialize_many, serialize_one


class AreasResource(Resource):
    def get(self):
        parent_id = request.args.get('parent_id')
        query = mongo.db.areas
        if parent_id:
            query = query.find({"parent_id": ObjectId(parent_id)})
        else:
            query = query.find()
        return serialize_many(query)

    def post(self):
        datas = request.json
        for data in datas:
            try:
                parent = mongo.db.cities.find_one(ObjectId(data.get('parent_id')))
            except InvalidId as e:
                raise BadRequest("Parent id not found in Cities")
            data['parent_id'] = parent.get('_id')
        areas = mongo.db.areas.insert_many(datas)
        return serialize_many(mongo.db.areas.find({"_id": {"$in": areas.inserted_ids}}))
