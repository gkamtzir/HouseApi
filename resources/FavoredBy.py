from flask_restful import Resource, abort, request
from models.Property import Property
from models.User import UserSchema
from common.Authentication import fetch_token

users_schema = UserSchema(many=True)


class FavoredByResource(Resource):
    def get(self, property_id):
        # Authorize user.
        id, role = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        if id is None:
            abort(401, status="error",
                  message="You have to log in to access this resource")
        property = Property.query.filter_by(id=property_id).first()
        if property is None:
            abort(404, message="Property with id = {} doesn't exist"
                  .format(property_id))
        users = property.favored_by
        users = users_schema.dump(users).data

        return {"status": "success", "data": users}, 200
