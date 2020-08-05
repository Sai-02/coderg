from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from flask_qa.extensions import db
from flask_qa.models import User

from config.config import params

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['name'].lower()
        password = request.form['pass']

        user = User.query.filter_by(username=username).first()

        error = None

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            error_message = 'Could not login. Please check and try again.'

    return render_template('lisu.html', params=params)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/signup/", methods=['GET', 'POST'])
def signup():
    # if user/admin already logged in
    # then redirect to home or dashboard
    # if 'user' in session:
    #     return redirect("/dashboard")

    if request.method == 'POST':
        fullname = request.form.get('fullname').title()
        username = request.form.get('uname').lower()
        email = request.form.get('email')
        password1 = request.form.get('pass1')
        password2 = request.form.get('pass2')

        error = None
        # checking against existing usernames and email
        if User.query.filter_by(email=email).first():
            error = 'Email already registered'
        elif User.query.filter_by(username=username).first():
            error = 'Username not available'
        else:
            if password1 == password2:
                user = User(fullname=fullname, username=username, email=email,
                            password=password1)
                db.session.add(user)
                db.session.commit()

                # TO DO flash in html and dashboard change checking
                flash("Sign up completed", "success")
                # signing in
                login_user(username)
                # session['user'] = username
                return redirect("/dashboard")
            else:
                error = "Wrong values entered"
                # return redirect("/dashboard")

        flash(error, "danger")
        # return redirect("/dashboard")

    return redirect("/dashboard")

# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         name = request.form['name']
#         password = request.form['password']
#
#         user = User(
#             fullname=name,
#             password=password,
#             admin=False,
#             expert=False)
#
#         db.session.add(user)
#         db.session.commit()
#
#         return redirect(url_for('auth.login'))
#
#     return render_template('register.html')


#


# Create 'member@example.com' user with no roles
# if not User.query.filter(User.email == 'member@example.com').first():
#     user = User(
#         email='member@example.com',
#         email_confirmed_at=datetime.datetime.utcnow(),
#         password=user_manager.hash_password('Password1'),
#     )
#     db.session.add(user)
#     db.session.commit()
#
# # Create 'admin@example.com' user with 'Admin' and 'Agent' roles
# if not User.query.filter(User.email == 'admin@example.com').first():
#     user = User(
#         email='admin@example.com',
#         email_confirmed_at=datetime.datetime.utcnow(),
#         password=user_manager.hash_password('Password1'),
#     )
#     user.roles.append(Role(name='Admin'))
#     user.roles.append(Role(name='Agent'))
#     db.session.add(user)
#     db.session.commit()
