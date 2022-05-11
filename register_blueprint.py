from applications.admin_app.admin_app import admin_app
from applications.client_app.client_app import client_app


def register_blueprint(app):
    app.register_blueprint(admin_app, url_prefix="/admin")
    app.register_blueprint(client_app, url_prefix="/client")
