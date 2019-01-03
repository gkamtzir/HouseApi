from flask_restful import Resource
from models.PropertySupervisor import PropertySupervisor,\
    PropertySupervisorSchema

property_supervisors_schema = PropertySupervisorSchema(many=True)


class PropertySupervisorResource(Resource):
    def get(self):
        property_supervisors = PropertySupervisor.query.all()
        property_supervisors = property_supervisors_schema\
            .dump(property_supervisors).data
        return {"status": "success", "data": property_supervisors}, 200
