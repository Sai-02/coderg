from flask import Flask

from .commands import create_tables
from .extensions import db
from .models import User, Projects, PostDb
from .routes.auth import auth
from .routes.main import main

from flask_user import UserManager
from flask_babelex import Babel


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    user_manager = UserManager(app, db, User)

    # Initialize Flask-BabelEx
    babel = Babel(app)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    app.cli.add_command(create_tables)

    return app

# def create_app(config_file='settings.py'):
#     app = Flask(__name__)
#
#     app.config.from_pyfile(config_file)
#
#     db.init_app(app)
#
#     login_manager.init_app(app)
#
#     login_manager.login_view = 'auth.login'
#
#     @login_manager.user_loader
#     def load_user(user_id):
#         return User.query.get(user_id)
#
#     app.register_blueprint(main)
#     app.register_blueprint(auth)
#
#     app.cli.add_command(create_tables)
#
#     return app
