from flask_restx import Api
from flask import Blueprint

# Import auth namespace
from .routes import api 

user_roles_bp = Blueprint("user_roles", __name__)

user_roles = Api(
    user_roles_bp, title="User operations", description="User Roles"
)

user_roles.add_namespace(api)