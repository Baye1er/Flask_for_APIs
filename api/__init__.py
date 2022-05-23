from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Too very hard to guess.'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe6:groupe6@localhost/apibase'
    db.app = app # When we get an error like "RuntimeError: application not registered on db instance and no applicationbound to current context"
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import api  # import the blueprint package

    app.register_blueprint(api)

    #with app.app_context():
    create_database(app)

    return app


def create_database(app):
    if not path.exists('api/apibase.db'):
        db.create_all(app=app)


