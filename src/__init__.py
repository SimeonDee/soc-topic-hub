from flask import Flask

from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app["SECRET_KEY"] = SECRET_KEY

    if test_config:
        app.config.from_object(test_config)

    return app
