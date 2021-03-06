from flask_restful import Resource, request, abort
from models.PropertyAction import PropertyAction,\
    PropertyActionSchema
from common.Authentication import fetch_token

property_actions_schema = PropertyActionSchema(many=True)


class PropertyActionResource(Resource):
    def get(self):
        # Authorize user.
        id, role = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        if id is None:
            abort(401, status="error",
                  message="You have to log in to access this resource")
        property_actions = PropertyAction.query.all()
        property_actions = property_actions_schema\
            .dump(property_actions).data
        return {"status": "success", "data": property_actions}, 200
