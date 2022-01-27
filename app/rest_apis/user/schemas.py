from flask_restx import Namespace, fields


class schema:
    api = Namespace("user", description="User object.")

    user_obj = api.model(
        "User object",
        {
            "first_name": fields.String(required=True),
            "last_name": fields.String(required=True),
            "cnic": fields.String(required=True),
            "date_of_birth": fields.String(required=True),
            "province": fields.String(required=True),
        },
    )

    user_register = api.model(
        "User registration data",
        {
            "first_name": fields.String(required=True),
            "last_name": fields.String(required=True),
            "cnic": fields.String(required=True),
            "date_of_birth": fields.String(required=True),
            "province": fields.String(required=True),
        },
    )

    user_get_success = api.model(
        "Get All Users success response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "users": fields.List(fields.Nested(user_obj)),
        },
    )

    user_success = api.model(
        "User success response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "user": fields.Nested(user_obj),
        },
    )