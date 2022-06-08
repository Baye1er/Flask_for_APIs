# USERS
from flask import jsonify, url_for, request, redirect, session

from app import db
from app.api.access_models import Utilisateur, ACCESS
from app.api.models import User, UserTrash
from app.api.views import api

from functools import wraps



# Decorator
def requires_access_level(access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not session.get('email'):
                return redirect(url_for('web.error_page'))

            utilisateur = Utilisateur.find_by_email(session['email'])
            if not utilisateur.allowed(access_level):
                return redirect(url_for('web.error_page', message="You do not have access to that page. Sorry!"))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


@api.route('/users/')
@requires_access_level(ACCESS['simple_user'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_json() for user in users]), 200


@api.route('/users/<int:id>')
@requires_access_level(ACCESS['simple_user'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json()), 200


@api.route('/users/', methods=['POST'])
@requires_access_level(ACCESS['moderator'])
def new_user():
    data = request.get_json()

    user = User(id=User.query.order_by(User.id.desc()).first().id+1,
                name=data['name'],
                username=data['username'],
                email=data['email'],
                street=data['street'],
                suite=data['suite'],
                city=data['city'],
                zipcode=data['zipcode'],
                lat=data['lat'],
                lng=data['lng'],
                phone=data['phone'],
                website=data['website'],
                company_name=data['company_name'],
                company_catchPhrase=data['company_catchPhrase'],
                company_bs=data['company_bs']
                )
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id,
                    'name': user.name,
                    'username': user.username,
                    'email': user.email,
                    'address': {'street': user.street,
                                'suite': user.suite,
                                'city': user.city,
                                'zipcode': user.zipcode,
                                'geo': {
                                    'lat': user.lat,
                                    'lng': user.lng
                                }
                                },
                    'phone': user.phone,
                    'website': user.website,
                    'company': {
                        'company_name': user.company_name,
                        'company_catchPhrase': user.company_catchPhrase,
                        'company_bs': user.company_bs,
                    }
                    }), 201


@api.route('/users/<int:id>', methods=['PUT'])
@requires_access_level(ACCESS['moderator'])
def update_user(id):
    user = User.query.get_or_404(id)
    user.id = request.json.get('id', user.id)
    user.name = request.json.get('name', user.name)
    user.username = request.json.get('username', user.username)
    user.email = request.json.get('email', user.email)
    user.street = request.json.get('street', user.street)
    user.suite = request.json.get('suite', user.suite)
    user.city = request.json.get('city', user.city)
    user.zipcode = request.json.get('zipcode', user.zipcode)
    user.lat = request.json.get('lat', user.lat),
    user.lng = request.json.get('lng', user.lng),
    user.phone = request.json.get('phone', user.phone),
    user.website = request.json.get('website', user.website),
    user.company_name = request.json.get('company_name', user.company_name),
    user.company_catchPhrase = request.json.get('company_catchPhrase', user.company_catchPhrase),
    user.company_bs = request.json.get('company_bs', user.company_bs),
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_json()), 204


@api.route('/users/<int:id>', methods=['DELETE'])
@requires_access_level(ACCESS['admin'])
def delete_user(id):
    user = User.query.filter_by(id=id).first_or_404()
    user_trash = UserTrash(
        id=user.id,
        name=user.name,
        username=user.username,
        email=user.email,
        street=user.street,
        suite=user.suite,
        city=user.city,
        zipcode=user.zipcode,
        lat=user.lat,
        lng=user.lng,
        phone=user.phone,
        website=user.website,
        company_name=user.company_name,
        company_catchPhrase=user.company_catchPhrase,
        company_bs=user.company_bs
    )
    db.session.add(user_trash)
    db.session.commit()

    # deleting post
    db.session.delete(user)
    db.session.commit()
    return {
        'success': 'user deleted successfully'
    }


# Displaying the trash for users
@api.route('/users_trash/')
def get_user_trash():
    users = UserTrash.query.all()
    return jsonify([user.to_json() for user in users]), 200


# Restoring user
@api.route('/users_restore/<int:id>', methods=['DELETE'])
def restore_user(id):
    user = UserTrash.query.filter_by(id=id).first_or_404()
    user_restore = User(
        id=user.id,
        name=user.name,
        username=user.username,
        email=user.email,
        street=user.street,
        suite=user.suite,
        city=user.city,
        zipcode=user.zipcode,
        lat=user.lat,
        lng=user.lng,
        phone=user.phone,
        website=user.website,
        company_name=user.company_name,
        company_catchPhrase=user.company_catchPhrase,
        company_bs=user.company_bs
    )
    db.session.add(user_restore)
    db.session.commit()

    # deleting post
    db.session.delete(user)
    db.session.commit()
    return {
        'success': 'user restored successfully'
    }



