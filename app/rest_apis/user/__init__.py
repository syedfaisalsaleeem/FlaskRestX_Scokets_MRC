from flask_restx import Api
from flask import Blueprint
from app import db

# Import auth namespace
from .routes import api 

user_bp = Blueprint("user", __name__)

user = Api(
    user_bp, title="User operations", description="CRUD operation on user"
)

user.add_namespace(api)





