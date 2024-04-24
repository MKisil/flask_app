from flask import Flask
from flask_login import LoginManager
from slugify import slugify
from sqlalchemy import event
from werkzeug.security import generate_password_hash

from app.extensions import db, admin, csrf
from app.models.post import Post
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    admin.init_app(app)
    csrf.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.models.main import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
