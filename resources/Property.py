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
        properties = Property.query.all()
        properties = properties_schema\
            .dump(properties).data
        return {"status": "success", "data": properties}, 200
