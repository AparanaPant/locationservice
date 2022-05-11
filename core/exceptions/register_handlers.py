from flask import jsonify

from core.exceptions.exception_baseclass import BadRequest, EntityDoesntExistError


def register_handlers(app):
    # if app.config.get('DEBUG') is True:
    #     return

    @app.errorhandler(BadRequest)
    def handle_error(e):
        return jsonify(e.__dict__), e.__dict__['code']

    @app.errorhandler(EntityDoesntExistError)
    def handle_error(e):
        return jsonify(e.__dict__), e.__dict__['code']
