from flask_restful import Resource, abort, request
from models.User import User
from models.Property import PropertySchema
from common.Authentication import fetch_token

properties_schema = PropertySchema(many=True)


class UserFavoritesResource(Resource):
    def get(self, user_id):
        # Authorize user.
        id = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            abort(404, message="User with id = {} doesn't exist"
                  .format(user_id))
        properties = user.properties
        properties = properties_schema.dump(properties).data
        return {"status": "success", "data": properties}, 200
