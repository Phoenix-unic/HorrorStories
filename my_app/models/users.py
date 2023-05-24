import os
from flask_login import UserMixin
from flask import current_app
from .db import db
from werkzeug.security import generate_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(16), nullable=False)
    posts = db.relationship('Post', backref=db.backref('user', lazy=True))
    

    @staticmethod
    def get_default_avatar():
        with current_app.open_resource(os.path.join('static', 'images/default-avatar.png'), 'rb') as avatar:
            return avatar.read()

    @classmethod
    def user_exists(cls: object, username: str, email: str) -> bool:
        search_key = (cls.query.filter_by(username=username).first() or cls.query.filter_by(email=email).first())
        return search_key
    
    @classmethod
    def find_user(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def register_user(cls, username, email, password):
        new_user = cls(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

    @classmethod
    def delete_user(cls, id):
        user = cls.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()

    @classmethod
    def update_username_email(cls, id, username, email):
        user = cls.query.get_or_404(id)
        user.username = username
        user.email = email
        db.session.commit()


    @classmethod
    def update_password(cls, id, password):
        user = cls.query.get_or_404(id)
        user.password = generate_password_hash(password)
        db.session.commit()


    def __repr__(self):
        return f'<User {self.username}>'

        



















