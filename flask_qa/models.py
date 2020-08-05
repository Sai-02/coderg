from flask_user import UserMixin
from werkzeug.security import generate_password_hash

from .extensions import db


# Define the User data-model.
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    username = db.Column(db.String(50), nullable=False, unique=True)
    _hashed_password = db.Column(db.String(255), nullable=False, server_default='')

    # User information
    first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
    last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')

    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_roles')

    @property
    def fullname(self):
        return self.first_name + self.last_name

    @fullname.setter
    def fullname(self, name):
        split_name = name.split()
        self.first_name = split_name[0]
        if split_name[1]:
            self.last_name = split_name[1]
        else:
            self.last_name = ''

    @property
    def password(self):
        return self._hashed_password

    @password.setter
    def password(self, unhashed_password):
        self._hashed_password = generate_password_hash(unhashed_password)


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


# class UserDb(db.Model):
#     fullname = db.Column(db.String(), nullable=False)
#     username = db.Column(db.String(), primary_key=True, unique=True, nullable=False)
#     email = db.Column(db.String(), nullable=False)
#     password = db.Column(db.String(200), nullable=False)
#     admin = db.Column(db.Boolean, default=False)


class Projects(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(), unique=False, nullable=False)
    title = db.Column(db.String(), unique=True, nullable=False)
    language = db.Column(db.String(), unique=False, nullable=False)
    purpose = db.Column(db.String(), unique=False, nullable=False)
    working_on = db.Column(db.String(), unique=False, nullable=False)
    link = db.Column(db.String(), unique=False, nullable=False)
    author = db.Column(db.String(), unique=False, nullable=False)


class PostDb(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    tagline = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False)
    fullname = db.Column(db.String(), nullable=False)
    slug = db.Column(db.String(), unique=True, nullable=False)
    content = db.Column(db.String(), nullable=False)
    date = db.Column(db.String(), nullable=True)
    img_file = db.Column(db.String(), nullable=True)
# author is the username of the user
# name should be fetched from UserDb
