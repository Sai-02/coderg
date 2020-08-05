from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash

from flask_qa.extensions import db
from flask_qa.models import User

auth = Blueprint('auth', __name__)


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


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        user = User.query.filter_by(name=name).first()

        error_message = ''

        if not user or not check_password_hash(user.password, password):
            error_message = 'Could not login. Please check and try again.'

        if not error_message:
            login_user(user)
            return redirect(url_for('main.index'))

    return render_template('login.html')


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################


@main.route("/logout/")
def logout():
    session.pop('user')
    return redirect("/dashboard")


@auth.route("/signup/", methods=['GET', 'POST'])
def signup():
    # user/admin already logged in
    if 'user' in session:
        return redirect("/dashboard")

    if request.method == 'POST':
        fullname = request.form.get('fullname').title()
        username = request.form.get('uname').lower()
        email = request.form.get('email')
        password1 = request.form.get('pass1')
        password2 = request.form.get('pass2')
        # checking against existing usernames
        user = UserDb.query.filter_by(username=username).first()
        if not user:
            if password1 == password2:
                user = UserDb(fullname=fullname, username=username, email=email,
                              password=sha256(password1.encode('utf-8')).hexdigest())
                db.session.add(user)
                db.session.commit()

                # TO DO flash in html and dashboard change checking
                flash("Sign up completed", "success")
                # signing in
                session['user'] = username
                return redirect("/dashboard")
            else:
                flash("Wrong values entered", "danger")
                return redirect("/dashboard")

        else:
            flash("Username not available", "danger")
            return redirect("/dashboard")

    return redirect("/dashboard")


#


# Create 'member@example.com' user with no roles
if not User.query.filter(User.email == 'member@example.com').first():
    user = User(
        email='member@example.com',
        email_confirmed_at=datetime.datetime.utcnow(),
        password=user_manager.hash_password('Password1'),
    )
    db.session.add(user)
    db.session.commit()

# Create 'admin@example.com' user with 'Admin' and 'Agent' roles
if not User.query.filter(User.email == 'admin@example.com').first():
    user = User(
        email='admin@example.com',
        email_confirmed_at=datetime.datetime.utcnow(),
        password=user_manager.hash_password('Password1'),
    )
    user.roles.append(Role(name='Admin'))
    user.roles.append(Role(name='Agent'))
    db.session.add(user)
    db.session.commit()
