from flask_restful import Resource, request, abort
from models.PropertySupervisor import PropertySupervisor,\
    PropertySupervisorSchema
from common.Authentication import fetch_token

property_supervisors_schema = PropertySupervisorSchema(many=True)


class PropertySupervisorResource(Resource):
    def get(self):
        # Authorize user.
        id, role = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        property_supervisors = PropertySupervisor.query.all()
        property_supervisors = property_supervisors_schema\
            .dump(property_supervisors).data
        return {"status": "success", "data": property_supervisors}, 200
