from flask_user import UserManager
from .models import User
from .extensions import db

user_manager = UserManager(db, User)
