from flask_restx import Namespace, fields


class schema:
    api = Namespace("", description="User authentication object.")

    user_obj = api.model(
        "User object",
        {
            "email": fields.String(required=True),
        },
    )

    user_register = api.model(
        "User registration data",
        {
            "email": fields.String(required=True),
            "password": fields.String(required=True),
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