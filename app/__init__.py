# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)

    db.init_app(flask_app)

    return flask_app






