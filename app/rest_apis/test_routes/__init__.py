from flask_restx import Api
from flask import Blueprint

# Import auth namespace
from .routes import api 

test_roles_bp = Blueprint("test_roles", __name__)

test_roles = Api(
    test_roles_bp, title="User operations", description="User Roles"
)

test_roles.add_namespace(api)