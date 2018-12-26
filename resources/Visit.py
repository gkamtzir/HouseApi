from flask_restful import Resource
from models.Visit import Visit,\
    VisitSchema

visits_schema = VisitSchema(many=True)
visit_schema = VisitSchema()


class VisitResource(Resource):
    def get(self):
        visits = Visit.query.all()
        visits = visits_schema\
            .dump(visits).data
        return {"status": "success", "data": visits}, 200
