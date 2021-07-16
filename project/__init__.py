from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from project.config import BaseConfig

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # FACTORY START
    app = Flask(__name__)

    # CONFIG
    app.config.from_object(BaseConfig())

    # uploader

    from project.controllers.heradeeansuploader import ansuploader
    app.register_blueprint(ansuploader.bp)

    return app
