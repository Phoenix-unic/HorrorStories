from flask import Flask
from flask_migrate import Migrate
from my_app.models.db import db, create_db
from my_app.auth_bp import auth, login_manager
from my_app.blog_bp import blog


def create_app():
    """create and configure the application"""
    app = Flask(__name__, instance_relative_config=True)  # init app
    app.config.from_pyfile('config.py')  # apply config from instance/config.py
    db.init_app(app)  # init SQLAlchemy app
    create_db(app)  # create all
    migrate = Migrate(app=app, db=db, command='migrate')

    # register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(blog)
    login_manager.init_app(app)

    @app.route('/test')
    def app_test_route():
        return '<h1>test<h1/>'

    return app










