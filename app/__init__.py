from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints inside the create_app function
    from .controllers.users_controller import user_bp
    # from .controllers.posts_controller import post_bp

    app.register_blueprint(user_bp)
    # app.register_blueprint(post_bp)

    return app

# Import models here to avoid circular imports
from app.models import *