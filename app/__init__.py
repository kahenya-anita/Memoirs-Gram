from flask import Flask
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config, config_options


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

photos = UploadSet('photos',IMAGES)


def create_app(config_name):
    app = Flask(__name__)
    
    db.init_app(app)
    app.config.from_object(config_options[config_name]) 
    app.config['SECRET_KEY'] = 'fbdc1dba0db1af419fc195f780d34c27d1ffe0efb6edbb585e22f8d027ecadce'
    
    # configure UploadSet
    configure_uploads(app,photos)
    
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.users.routes import users
    from app.posts.routes import posts
    from app.main.routes import main
    from app.errors.handlers import errors
    from app.models import User, Post  
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app