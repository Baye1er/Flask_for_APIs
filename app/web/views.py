from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify
from flask_login import login_user, login_required, current_user
from werkzeug.security import check_password_hash

from app import db
from app.api.models import User
from app.web.forms import NewUserForm

web = Blueprint('web', __name__)


@web.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('.display_user'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('home.html', user=current_user)


@web.route('/users', methods=['POST', 'GET'])
#@login_required
def display_users():
    users = User.query.all()

    return render_template('display_users.html', users=users)


@web.route('/update_user/<id>', methods=['POST'])
#@login_required
def update_users(id):
    user = User.query.get_or_404(id)
    user.name = request.form['name']
    value = request.form['value']
    if user.name == 'name':
        user.name = value
        db.session.add(user)

    elif user.name == 'username':
        user.username = value
        db.session.add(user)

    elif user.name == 'email':
        user.email = value
        db.session.add(user)

    else:
        user.city = value
        db.session.add(user)
    db.session.commit()

    return jsonify({'status': 'OK'})


@web.route('/new-user', methods=['GET', 'POST'])
def new_user():
    form = NewUserForm()
    if form.validate_on_submit():
        user = User(
                    name=form.name.data,
                    username=form.username.data,
                    email=form.email.data,
                    street=form.street.data,
                    suite=form.suite.data,
                    city=form.city.data,
                    zipcode=form.zipcode.data,
                    lat=form.lat.data,
                    lng=form.lng.data,
                    phone=form.phone.data,
                    website=form.website.data,
                    company_name=form.company_name.data,
                    company_catchPhrase=form.company_catchPhrase.data,
                    company_bs=form.company_bs.data,
                    password=form.password.data
                    )
        db.session.add(user)
        db.session.commit()
        flash('User added successfully!', 'success')
        return redirect(url_for('.display_users'))
    return render_template('new_user.html', form=form)
