from flask_restful import Resource
from models.Property import Property,\
    PropertySchema

properties_schema = PropertySchema(many=True)


class PropertyResource(Resource):
    def get(self):
        properties = Property.query.all()
        properties = properties_schema\
            .dump(properties).data
        return {"status": "success", "data": properties}, 200
