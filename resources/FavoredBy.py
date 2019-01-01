from flask_restful import Resource, abort
from models.Property import Property
from models.User import UserSchema

users_schema = UserSchema(many=True)


class FavoredBy(Resource):
    def get(self, property_id):
        property = Property.query.filter_by(id=property_id).first()
        if property is None:
            abort(404, message="Property with id = {} doesn't exist"
                  .format(property_id))
        users = property.favored_by
        users = users_schema.dump(users).data

        return {"status": "success", "data": users}, 200
