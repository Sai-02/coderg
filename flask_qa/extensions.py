from flask_sqlalchemy import SQLAlchemy

from flask_user import SQLAlchemyAdapter
from .models import User

db = SQLAlchemy()
db_adapter = SQLAlchemyAdapter(db, User)
