from flask_restful import Resource, request
from models.User import User, UserSchema
from common.Authentication import encode_auth_token

user_schema = UserSchema()


class LoginResource(Resource):
    def post(self):
        post_data = request.get_json()
        try:
            user = User.query.filter_by(contact_email=post_data.get("email"))\
                .first()
            if user is None:
                return {"status": "Fail", "message": "User does not exist."}, \
                    404
            else:
                user = user_schema.dump(user).data
                return {"status": "Success",
                        "token": str(encode_auth_token(user["id"]))}, 200
        except Exception as e:
            print(e)
            return {"status": "Fail", "message": "Try again"}, 500
