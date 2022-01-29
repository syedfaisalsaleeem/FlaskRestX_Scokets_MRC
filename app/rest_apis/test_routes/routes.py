from flask_restx import Resource
from .schemas import schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.rest_apis.user_roles.models.users_model import User
api = schema.api

@api.route("/testadmin")
class AdminRoute(Resource):
    
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        data = User.query.filter(User.id==current_user).first()
        for values in data.roles:
            if  "admin" != values.name:
                return {"status":False,"message":"Only Admin can access Unauthorized"},403
            else:
                return {"status":True,"message":"You have successfully accessed"},200

@api.route("/testemployees")
class AdminRoute(Resource):
    
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        data = User.query.filter(User.id==current_user).first()
        for values in data.roles:
            if  "employees" != values.name:
                return {"status":False,"message":"Only Employees can access Unauthorized"},403
            else:
                return {"status":True,"message":"You have successfully accessed"},200