from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app,db)
# login = LoginManager(app)


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app,db)

    from app.auth import bp as auth_bp
    from app.main import bp as main_bp
    from app.errors import bp as errors_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(errors_bp)

    return app

#from app import routes,models,errors
from app import models