class BaseError(Exception):
    def __init__(self, code=400, message="", status="", field=None):
        Exception.__init__(self)
        self.code = code
        self.message = message
        self.status = status
        self.field = field
        self.success = False

    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "status": self.status,
            "field": self.field,
            "success": self.success
        }


class EntityDoesntExistError(BaseError):
    def __init__(self, message="Entity with requested id doesn't exist in system",
                 code=400,
                 status="ENTITY_DOESNT_EXIST"):
        super().__init__(self)
        self.message = message if message is not None else "Entity with requested id doesn't exist in system"
        self.code = code
        self.status = status
        self.success = False

    def to_dict(self):
        return {
            "message": self.message,
            "code": self.code,
            "status": self.status,
            "success": self.success
        }


class BadRequest(BaseError):
    def __init__(self, message='invalid query string', code=400, status='INVALID_PARAMETER'):
        super().__init__(self)
        self.message = message
        self.code = code
        self.status = status
