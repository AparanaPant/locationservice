from bson import ObjectId
from bson.errors import InvalidId

from core.exceptions.exception_baseclass import BadRequest


def find_by_id_or_404(model, document_id):
    try:
        return model.find_one(ObjectId(document_id))
    except InvalidId as e:
        raise BadRequest("not found")
