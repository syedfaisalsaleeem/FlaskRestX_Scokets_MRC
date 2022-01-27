from flask import Flask

# Import extensions
from app.extensions import cors, db, jwt, ma, sk, api


def create_app(config_name):
    app = Flask(__name__)
    app.config[
    "SQLALCHEMY_DATABASE_URI"
] = config_name

    register_extensions(app)

    # Register blueprints
    from .rest_apis.user import user_bp

    app.register_blueprint(user_bp)

    from .sockets import index

    from .rest_apis.user_roles import user_roles_bp

    app.register_blueprint(user_roles_bp, url_prefix="/user_roles")

    from .rest_apis.test_routes import test_roles_bp
    app.register_blueprint(test_roles_bp, url_prefix="/test_roles")

    return app


def register_extensions(app):
    # Registers flask extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    sk.init_app(app)
    api.init_app(app)