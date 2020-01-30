from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.api.V1.routes import load_routes_v1


db = SQLAlchemy()

def create_app(config_filename=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_db(app)
    initialize_api(app)
    return app

def initialize_api(app):
    api = Api(app, prefix="/api/v1/")
    load_routes_v1(api)

def initialize_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)