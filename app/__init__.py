from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.api.V1.routes import load_routes_v1
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    initialize_db(app)
    initialize_api(app)
    return app

def initialize_api(app):
    api = Api(app, prefix="/api/v1/")
    load_routes_v1(api)

def initialize_db(app):
    db.init_app(app)