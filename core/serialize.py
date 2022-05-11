# import json
# import re
#
# from bson.json_util import dumps, CANONICAL_JSON_OPTIONS


# def serialize(data):
#     clean_json = re.compile('ISODate\(("[^"]+")\)').sub('\\1',
#                                                         dumps(data,
#                                                               json_options=CANONICAL_JSON_OPTIONS))
#     return json.loads(clean_json)

# todo:improve serialization and deserialization
def serialize_many(items):
    response = []
    for item in items:
        item['id'] = str(item.pop('_id'))
        if item.get('parent_id'):
            item['parent_id'] = str(item.pop('parent_id'))
        response.append(item)
    return response


def serialize_one(item):
    item['id'] = str(item.pop('_id'))
    if item.get('parent_id'):
        item['parent_id'] = str(item.pop('parent_id'))
    return item
