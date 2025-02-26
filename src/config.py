from flask import Flask
from decouple import config
from src.errors.error_handler import register_error_handlers


def configure_app(app: Flask):
    register_error_handlers(app)


class Config:
    SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATIONS")
