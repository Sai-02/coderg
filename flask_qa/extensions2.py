from flask_user import SQLAlchemyAdapter, UserManager
from .models import User
from .extensions import db

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter)
