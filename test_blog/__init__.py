
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from test_blog.config import Config
from flask_bcrypt import Bcrypt
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    from test_blog.main.routes import main
    from test_blog.users.routes import users
    from test_blog.posts.routes import posts
    from test_blog.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    app.config.from_object(Config)

    return app
