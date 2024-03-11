from flask import Flask
from extensions import db, jwt
from auth import auth_bp
from users import user_bp


def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()

    #initialize apps
    db.init_app(app)
    jwt.init_app(app)


    #register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)

    return app