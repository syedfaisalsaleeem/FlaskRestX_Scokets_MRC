
from app import ma
from .models.roles_model import Role
from .models.users_model import User
from marshmallow import fields

class RolesSerializer(ma.Schema):
    class Meta:
        model = Role
        # Fields to expose, add more if needed.
        fields = ("name",)



class UsersSerializer(ma.Schema):
    roles = fields.Nested(RolesSerializer, many=True)
    class Meta:
        model = User
        # Fields to expose, add more if needed.
        fields = ("email","password", "roles",)