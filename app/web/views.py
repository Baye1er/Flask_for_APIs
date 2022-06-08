from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify
from flask_login import login_user, login_required, current_user
from werkzeug.security import check_password_hash

from app import db
from app.api.access_models import Utilisateur
from app.api.models import User
import psycopg2

web = Blueprint('web', __name__)


# Auth page
@web.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        utilisateur = Utilisateur.query.filter_by(email=email).first()
        if utilisateur:
            if check_password_hash(utilisateur.password, password):
                flash('Logged in successfully!', category='success')
                login_user(utilisateur, remember=True)
                return redirect(url_for('.display_users'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('pageLogin.html', utilisateur=current_user)


@web.route('/error', methods=['POST', 'GET'])
def error_page():
    return render_template('error_page.html')


@web.route('/users', methods=['POST', 'GET'])
@login_required
def display_users():
    """
   :return: We will all our users
   """

    return render_template('users.html')


@web.route('/update_users', methods=['POST'])
@login_required
def update_users():
    conn = psycopg2.connect(
        database='apibase', user='groupe6', password='groupe6', host='127.0.0.1', port='5432')
    conn.autocommit = True

    cursor = conn.cursor()

    pk = request.form['id']
    name = request.form['name']
    value = request.form['value']
    if name == 'name':
        cursor.execute("UPDATE users SET name = %s WHERE id = %s ", (value, pk))
    elif name == 'username':
        cursor.execute("UPDATE users SET username = %s WHERE id = %s ", (value, pk))
    elif name == 'email':
        cursor.execute("UPDATE users SET email = %s WHERE id = %s ", (value, pk))
    elif name == 'city':
        cursor.execute("UPDATE users SET city = %s WHERE id = %s ", (value, pk))
    conn.commit()
    conn.close()

    return jsonify({'status': 'OK'})
