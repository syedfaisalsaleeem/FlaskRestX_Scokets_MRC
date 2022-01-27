from flask import current_app
from app import db
from app.rest_apis.utility.index import message, err_resp, internal_err_resp
from .models.users_model import User
from .models.roles_model import Role
from .serializers import UsersSerializer,RolesSerializer
from flask_jwt_extended import create_access_token

users_serializer = UsersSerializer()
roles_serializer = RolesSerializer()


class AuthController:

    @staticmethod
    def login(data):
        # Assign vars
        email = data["email"]
        password = data["password"]

        try:
            # Fetch user data
            if not (user := User.query.filter_by(email=email).first()):
                return err_resp(
                    "The email you have entered does not match any account.",
                    "email_404",
                    404,
                )

            elif user and user.verify_password(password):
                user_info = users_serializer.dump(user)

                access_token = create_access_token(identity=user.id)

                resp = message(True, "Successfully logged in.")
                resp["access_token"] = access_token
                resp["user"] = user_info

                return resp, 200

            return err_resp(
                "Failed to log in, password may be incorrect.", "password_invalid", 401
            )

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def register(data):
        # Assign vars
        ## Required values
        email = data["email"]
        password = data["password"]
        roles = data["roles"][0]["name"]

        # Check if the email is taken
        if User.query.filter_by(email=email).first() is not None:
            return err_resp("Email is already being used.", "email_taken", 403)


        try:
            new_user = User(
                email=email,
                password=password,
 
            )
            if Role.query.filter_by(name=roles).first() is not None:
                r = Role.query.filter_by(name=roles).first()
            else:
                r = Role(
                    name=roles,
                )
            new_user.roles.append(r)
            db.session.add(new_user)
            db.session.flush()
            # Load the new user's info
            user_info = users_serializer.dump(new_user)
            
            # Commit changes to DB
            db.session.commit()
            # Create an access token
            access_token = create_access_token(identity=new_user.id)

            resp = message(True, "User has been registered.")
            resp["access_token"] = access_token
            resp["user"] = user_info

            return resp, 201

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()