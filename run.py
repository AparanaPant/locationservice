from dotenv import load_dotenv
from flask import Flask
from werkzeug.utils import import_string

from core.exceptions.register_handlers import register_handlers
from core.extensions.database.mongodb_config import mongo
from register_blueprint import register_blueprint

load_dotenv('.env')


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(import_string(config)())
    register_blueprint(app)
    mongo.init_app(app)
    register_handlers(app)
    return app
