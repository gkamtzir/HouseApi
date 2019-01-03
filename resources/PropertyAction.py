from flask_restful import Resource
from models.PropertyAction import PropertyAction,\
    PropertyActionSchema

property_actions_schema = PropertyActionSchema(many=True)


class PropertyActionResource(Resource):
    def get(self):
        property_actions = PropertyAction.query.all()
        property_actions = property_actions_schema\
            .dump(property_actions).data
        return {"status": "success", "data": property_actions}, 200
