#from app import db
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True, index=True)
    street = db.Column(db.String(128))
    suite = db.Column(db.String(128))
    city = db.Column(db.String(128))
    zipcode = db.Column(db.String(128))
    lat = db.Column(db.String(128))
    lng = db.Column(db.String(128))
    phone = db.Column(db.String(128))
    website = db.Column(db.String(128))
    company_name = db.Column(db.String(128))
    company_catchPhrase = db.Column(db.String(128))
    company_bs = db.Column(db.String(128))
    #password = db.Column(db.String(128), default='Default')
    posts = db.relationship('Post', backref='owned_user', lazy='dynamic')
    albums = db.relationship('Album', backref='owned_user', lazy='dynamic')
    todos = db.relationship('Todo', backref='owned_user', lazy='dynamic')

    def to_json(self):
        json_user = {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'address': {
                'street': self.street,
                'suite': self.suite,
                'city': self.city,
                'zipcode': self.zipcode,
                'geo': {
                    'lat': self.lat,
                    'lng': self.lng
                }
            },
            'phone': self.phone,
            'website': self.website,
            'company': {
                'name': self.company_name,
                'catchPhrase': self.company_catchPhrase,
                'bs': self.company_bs
            }
        }

        return json_user


class UserTrash(db.Model):
    __tablename__ = 'users_trash'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True, index=True)
    street = db.Column(db.String(128))
    suite = db.Column(db.String(128))
    city = db.Column(db.String(128))
    zipcode = db.Column(db.String(128))
    lat = db.Column(db.String(128))
    lng = db.Column(db.String(128))
    phone = db.Column(db.String(128))
    website = db.Column(db.String(128))
    company_name = db.Column(db.String(128))
    company_catchPhrase = db.Column(db.String(128))
    company_bs = db.Column(db.String(128))

    def to_json(self):
        json_user = {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'address': {
                'street': self.street,
                'suite': self.suite,
                'city': self.city,
                'zipcode': self.zipcode,
                'geo': {
                    'lat': self.lat,
                    'lng': self.lng
                }
            },
            'phone': self.phone,
            'website': self.website,
            'company': {
                'name': self.company_name,
                'catchPhrase': self.company_catchPhrase,
                'bs': self.company_bs
            }
        }

        return json_user


class Post(db.Model):
    __tablename__ = 'posts'

    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.Text)
    comments = db.relationship('Comment', backref='owned_post', lazy='dynamic')

    def to_json(self):
        json_post = {
            'userId': self.userId,
            'id': self.id,
            'title': self.title,
            'body': self.body
        }

        return json_post


class PostTrash(db.Model):
    __tablename__ = 'posts_trash'

    userId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.Text)

    def to_json(self):
        json_post = {
            'userId': self.userId,
            'id': self.id,
            'title': self.title,
            'body': self.body
        }

        return json_post


class Comment(db.Model):
    __tablename__ = 'comments'

    postId = db.Column(db.Integer, db.ForeignKey('posts.id'))
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    body = db.Column(db.Text)

    def to_json(self):
        json_comment = {
            'postId': self.postId,
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'body': self.body
        }

        return json_comment


class CommentTrash(db.Model):
    __tablename__ = 'comments_trash'

    postId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128))
    body = db.Column(db.Text)

    def to_json(self):
        json_comment = {
            'postId': self.postId,
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'body': self.body
        }

        return json_comment


class Album(db.Model):
    __tablename__ = 'albums'

    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    photos = db.relationship('Photo', backref='owned_album', lazy='dynamic')

    def to_json(self):
        json_album = {
            'userId': self.userId,
            'id': self.id,
            'title': self.title,
        }

        return json_album


class AlbumTrash(db.Model):
    __tablename__ = 'albums_trash'

    userId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))

    def to_json(self):
        json_album = {
            'userId': self.userId,
            'id': self.id,
            'title': self.title,
        }

        return json_album


class Photo(db.Model):
    __tablename__ = 'photos'

    albumId = db.Column(db.Integer, db.ForeignKey('albums.id'))
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    url = db.Column(db.String(128))
    thumbnailUrl = db.Column(db.Text)

    def to_json(self):
        json_photo = {
            'albumId': self.albumId,
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'thumbnailUrl': self.thumbnailUrl
        }

        return json_photo


class PhotoTrash(db.Model):
    __tablename__ = 'photos_trash'

    albumId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    url = db.Column(db.String(128))
    thumbnailUrl = db.Column(db.Text)

    def to_json(self):
        json_photo = {
            'albumId': self.albumId,
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'thumbnailUrl': self.thumbnailUrl
        }

        return json_photo


class Todo(db.Model):
    __tablename__ = 'todos'

    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))

    # completed = db.Column(db.Boolean, default=False)

    def to_json(self):
        json_todo = {
            'userId': self.userId,
            'id': self.id,
            'title': self.title
        }

        return json_todo


class TodoTrash(db.Model):
    __tablename__ = 'todos_trash'

    userId = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))

    # completed = db.Column(db.Boolean, default=False)

    def to_json(self):
        json_todo = {
            'userId': self.userId,
            'id': self.id,
            'title': self.title
        }

        return json_todo
