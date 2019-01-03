from flask_restful import Resource
from models.HeatingType import HeatingType,\
    HeatingTypeSchema

heating_types_schema = HeatingTypeSchema(many=True)


class HeatingTypeResource(Resource):
    def get(self):
        heating_types = HeatingType.query.all()
        heating_types = heating_types_schema\
            .dump(heating_types).data
        return {"status": "success", "data": heating_types}, 200
