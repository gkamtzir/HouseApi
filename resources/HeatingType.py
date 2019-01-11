from flask_restful import Resource, request, abort
from models.HeatingType import HeatingType,\
    HeatingTypeSchema
from common.Authentication import fetch_token

heating_types_schema = HeatingTypeSchema(many=True)


class HeatingTypeResource(Resource):
    def get(self):
        # Authorize user.
        id = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        heating_types = HeatingType.query.all()
        heating_types = heating_types_schema\
            .dump(heating_types).data
        return {"status": "success", "data": heating_types}, 200
