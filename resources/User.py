from flask_restful import Resource, request, abort
from models.User import User, UserSchema
from common.Authentication import fetch_token

users_schema = UserSchema(many=True)


class UserResource(Resource):
    def get(self):
        # Authorize user.
        id = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        users = User.query.all()
        users = users_schema.dump(users).data
        return {"status": "success", "data": users}, 200
