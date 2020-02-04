import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

class Development(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:123@db/book_store_development"

class Production(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:123@db/book_store_production"

class Test(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:123@db/book_store_test"

config = dict(
    development=Development,
    production=Production,
)