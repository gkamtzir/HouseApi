from flask_restful import Resource
from models.User import User, UserSchema

users_schema = UserSchema(many=True)


class UserResource(Resource):
    def get(self):
        users = User.query.all()
        users = users_schema.dump(users).data
        return {"status": "success", "data": users}, 200
