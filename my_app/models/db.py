import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'horror_story.db'


from .posts import Post
from .users import User


def create_db(app):
    if not os.path.exists(f'instance/{DB_NAME}'):
        with app.app_context():
            db.create_all()
            print(f'DB {DB_NAME} was created...')
