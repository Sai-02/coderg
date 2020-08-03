from flask import Flask

from .commands import create_tables
from .extensions import db
from .models import Projects, UserDb, PostDb, User
from .routes.auth import auth
from .routes.main import main

from flask_user import UserManager, SQLAlchemyAdapter


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.config['USER_APP_NAME'] = 'Aqdas'
    # app.config['CSRF_ENABLED'] = True
    app.config['USER_ENABLE_EMAIL'] = False
    app.config['USER_ENABLE_USERNAME'] = True
    app.config['USER_REQUIRE_RETYPE_PASSWORD'] = False
    db_adapter = SQLAlchemyAdapter(db, User)
    user_manager = UserManager(db_adapter, app)

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
