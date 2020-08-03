from flask import Flask

from .commands import create_tables
from .extensions import db
from .extensions2 import user_manager
from .models import Projects, UserDb, PostDb, User
from .routes.auth import auth
from .routes.main import main


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    user_manager.init_app(app)

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
