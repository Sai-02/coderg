from flask_sqlalchemy import SQLAlchemy
from flask_user import SQLAlchemyAdapter, UserManager
from .models import User


db = SQLAlchemy()
db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter)
