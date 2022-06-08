from app import db
from flask_login import UserMixin

ACCESS = {
    'guest': 0,
    'simple_user': 1,
    'moderator': 2,
    'admin': 4
}


class Utilisateur(db.Model, UserMixin):
    __tablename__ = 'utilisateurs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64), unique=True)
    access = db.Column(db.Integer, default=1)

    def is_admin(self):
        return self.access == ACCESS['admin']

    def allowed(self, access_level):
        return self.access >= access_level
