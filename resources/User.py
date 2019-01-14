from flask_restful import Resource, request, abort
from models.User import User, UserSchema
from common.Authentication import fetch_token

user_schema = UserSchema()


class UserResource(Resource):
    def get(self):
        # Authorize user.
        id, role = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        if id is None:
            abort(401, status="error",
                  message="You have to log in to access this resource")
        if role == "supervisor":
                abort(401, status="error",
                      message="Only users can use this resource")

        user = User.query.filter_by(id=id).first()
        user = user_schema.dump(user).data
        return {"status": "success", "data": user}, 200
