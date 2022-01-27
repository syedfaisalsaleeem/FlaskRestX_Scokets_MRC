from flask import request
from flask_restx import Resource

from app.rest_apis.utility.index import validation_error

# Auth modules
from .controllers import UserController
from .schemas import schema
from .serializers import UserSerializer, dateofbirthserializer, provinceserializer

api = schema.api
user_success = schema.user_success
user_get_success = schema.user_get_success

user_schema = UserSerializer()

@api.route("")
class User(Resource):
    """ User register and get users
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
        
        dob = dateofbirthserializer(register_data['date_of_birth'])
        if (dob[0] == False):
            return validation_error(False,errors=dob[1]),400

        if (provinceserializer(register_data['province']) == False):
            return validation_error(False,errors={"province":["province format is invalid"]}),400
        

        return UserController.register(register_data)


    @api.doc(
        "Get users",
        responses={
            200: ("Users data successfully sent", user_get_success),
            404: "Users not found!",
        },
    )
    def get(self):
        """ Get all users data """
        return UserController.get_user_data()