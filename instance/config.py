import secrets
from my_app.models.db import DB_NAME


SECRET_KEY = secrets.token_hex(32)
SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
TRACK_MODIFICATIONS = False