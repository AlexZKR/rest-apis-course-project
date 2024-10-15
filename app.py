from flask import Flask
from flask_smorest import Api
from db import db
from config.config import Config  # Import configuration
from config.jwt_config import configure_jwt  # Import JWT configuration
from flask_migrate import Migrate


from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint


def create_app(db_url=None):
    app = Flask(__name__)

    # Load config from the Config class
    app.config.from_object(Config)

    # Override the SQLALCHEMY_DATABASE_URI if db_url is provided
    if db_url:
        app.config["SQLALCHEMY_DATABASE_URI"] = db_url

    db.init_app(app)

    #not needed because tables are created with migrate
    # with app.app_context():
    #     db.create_all()

    api = Api(app)

    # Apply the JWT configurations
    configure_jwt(app)
    
    Migrate(app, db)

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)

    return app
