import click
from flask import Flask
from src.config import Config, configure_app
from src.utils import db
from src.presentation.controllers.task import task_controllers
from flask_migrate import Migrate

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    configure_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    register_commands(app)
    app.register_blueprint(task_controllers.bp)

    return app


def register_commands(app):
    @app.cli.command("create_db")
    def create_db():
        with app.app_context():
            db.create_all()
            click.echo("Banco de dados inicializado com sucesso!")
