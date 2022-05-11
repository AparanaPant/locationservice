from flask import Blueprint
from flask_restful import Api

client_app = Blueprint('client_app', __name__)
api = Api(client_app)
