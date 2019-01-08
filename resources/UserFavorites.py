from flask_restful import Resource, abort
from models.User import User
from models.Property import PropertySchema

properties_schema = PropertySchema(many=True)


class UserFavoritesResource(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            abort(404, message="User with id = {} doesn't exist"
                  .format(user_id))
        properties = user.properties
        properties = properties_schema.dump(properties).data
        return {"status": "success", "data": properties}, 200
