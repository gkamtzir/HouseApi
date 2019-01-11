from flask_restful import Resource, abort, request
from models.User import User
from models.Property import PropertySchema
from common.Authentication import fetch_token

properties_schema = PropertySchema(many=True)


class UserFavoritesResource(Resource):
    def get(self):
        # Authorize user.
        id, role = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        if role == "supervisor":
            abort(401, status="error",
                  message="Only users can use this resource")

        user = User.query.filter_by(id=id).first()
        if user is None:
            abort(404, message="User with id = {} doesn't exist"
                  .format(id))
        properties = user.properties
        properties = properties_schema.dump(properties).data
        return {"status": "success", "data": properties}, 200
