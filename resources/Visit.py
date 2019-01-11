from flask_restful import Resource, request, abort
from models.Visit import Visit,\
    VisitSchema
from common.Authentication import fetch_token

visits_schema = VisitSchema(many=True)


class VisitResource(Resource):
    def get(self):
        # Authorize user.
        id = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        visits = Visit.query.all()
        visits = visits_schema\
            .dump(visits).data
        return {"status": "success", "data": visits}, 200
