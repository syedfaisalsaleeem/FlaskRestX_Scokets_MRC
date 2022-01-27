from flask import current_app
from app import db
from app.rest_apis.utility.index import message, err_resp, internal_err_resp
from .models import User
from .serializers import UserRetrieveSerializer, UserSerializer 

user_serializer = UserSerializer()
getuser_serializer = UserRetrieveSerializer()


class UserController:

    @staticmethod
    def register(data):
        # Assign vars

        ## Required values
        first_name = data["first_name"]
        last_name = data["last_name"]
        cnic = data["cnic"]
        date_of_birth = data["date_of_birth"]
        province = data["province"]

        try:
            new_user = User(
                first_name=first_name,
                last_name=last_name,
                cnic=cnic,
                date_of_birth=date_of_birth,
                province=province,
            )

            db.session.add(new_user)
            db.session.flush()

            # Load the new user's info
            user_info = user_serializer.dump(new_user)

            # Commit changes to DB
            db.session.commit()
   
            resp = message(True, "User has been registered.")
            resp["user"] = user_info
            return resp, 201

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def get_user_data():
        """ Get user data by username """
        if not (user := User.query.all()):
            return err_resp("Users not found!", "user_404", 404)

        try:
            user_info = getuser_serializer.dump(user,many=True)

            resp = message(True, "All user data is retrieved")
            resp["users"] = user_info
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()