# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config
from flask_heroku import Heroku

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()
heroku = Heroku()

def create_app(config_class=Config):
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)

    db.init_app(flask_app)  # initialize database
    bootstrap.init_app(flask_app)  # initialize bootstrap
    login_manager.init_app(flask_app)  # initialize login_manager
    bcrypt.init_app(flask_app)
    heroku.init_app(app)

    from app.catalog import main  # import blueprint
    flask_app.register_blueprint(main)  # register blueprint

    from app.auth import authentication
    flask_app.register_blueprint(authentication)

    return flask_app
