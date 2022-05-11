import json

from core.extensions.database.mongodb_config import mongo


def insert_provinces():
    provinces_collection = mongo.db.provinces
    provinces = json.load(open("scripts/provinces.txt"))
    for province in provinces:
        province['disabled'] = False
    provinces_collection.insert_many(provinces)


def insert_cities():
    cities = json.load(open("scripts/cities.txt"))
    for city in cities:
        province = mongo.db.provinces.find_one({'reference_id': city.get('parentId')})
        city['parent_id'] = province['_id']
        city.pop('parentId')
        city['disabled'] = False
    cities_collection = mongo.db.cities
    cities_collection.insert_many(cities)


def insert_areas():
    areas = json.load(open("scripts/areas.txt"))
    for area in areas:
        city = mongo.db.cities.find_one({'reference_id': area.get('parentId')})
        area['parent_id'] = city['_id']
        area.pop('parentId')
        area['disabled'] = False
    cities_collection = mongo.db.areas
    cities_collection.insert_many(areas)



