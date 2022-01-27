from flask import request
from flask_restx import Resource

from app.rest_apis.utility.index import validation_error

# Auth modules
from .controllers import AuthController
from .schemas import schema
from .serializers import UsersSerializer

api = schema.api
user_success = schema.user_success


user_schema = UsersSerializer()

@api.route("/register")
class UserRegister(Resource):
    """ User register and get user
    User registers then receives the user's information 
    """

    user_register = schema.user_register

    @api.doc(
        "User registration",
        responses={
            201: ("Successfully registered user.", user_success),
            400: "Malformed data or validations failed.",
        },
    )
    @api.expect(user_register, validate=True)
    def post(self):
        """ User registration """
        # Grab the json data
        register_data = request.get_json()
        
        # Validate data
        if (errors := user_schema.validate(register_data)) :
            return validation_error(False, errors), 400
        return AuthController.register(register_data)