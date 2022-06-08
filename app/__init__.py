from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from os import path
from flask_login import LoginManager
from app.api.models import User
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'Too very hard to guess.'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://groupe6:groupe6@localhost/apibase'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app  # When we get an error like "RuntimeError: application not registered on db instance and no applicationbound to current context"
    db.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app, db)

    from .api.views import api  # import the blueprint package
    from .web.views import web
    from .api.users_views import api

    app.register_blueprint(api)
    app.register_blueprint(web, url_prefix='/web')

    # with app.app_context():
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'web.home'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('api/apibase.db'):
        db.create_all(app=app)
