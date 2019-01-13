from flask_restful import Resource, request, abort
from models.PropertySupervisor import PropertySupervisor,\
    PropertySupervisorSchema
from common.Authentication import fetch_token

property_supervisor_schema = PropertySupervisorSchema()


class PropertySupervisorResource(Resource):
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
                  message="Only supervisors can use this resource")

        property_supervisor = PropertySupervisor.query.filter_by(id=id).first()
        property_supervisor = property_supervisor_schema\
            .dump(property_supervisor).data
        return {"status": "success", "data": property_supervisor}, 200
