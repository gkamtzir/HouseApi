from flask_restful import Resource, request, abort
from models.Property import Property,\
    PropertySchema
from common.Authentication import fetch_token

properties_schema = PropertySchema(many=True)


class PropertyResource(Resource):
    def get(self):
        # Authorize user.
        id, role = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        if id is None:
            abort(401, status="error",
                  message="You have to log in to access this resource")
        if role == "user":
            abort(401, status="error",
                  message="Only supervisors can access this resource.")
        properties = Property.query.filter(Property.supervisor_id == id)
        properties = properties_schema\
            .dump(properties).data
        return {"status": "success", "data": properties}, 200
