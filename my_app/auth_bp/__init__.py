from flask import Blueprint
from flask_login import LoginManager
from my_app.models.users import User

auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import views


login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # set the login view with app_context

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


