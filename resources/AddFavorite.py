from flask_restful import Resource, abort, request
from sqlalchemy.exc import IntegrityError
from models.Favorite import Favorite
from models.User import UserSchema
from models.Shared import db
from common.Authentication import fetch_token

user_schema = UserSchema()


class AddFavoriteResource(Resource):
    def post(self):
        try:
            # Authorize user.
            id, role = fetch_token(request.headers.get("Authorization"))
            if id is not None and not isinstance(id, int):
                abort(401, status="error", message=id)
            if id is None:
                abort(401, status="error",
                      message="You have to log in to access this resource")
            if role == "supervisor":
                abort(401, status="error",
                      message="Only users can use this resource")

            post_data = request.get_json()

            # Checking if property_id exists.
            property_id = post_data.get("property_id")
            if property_id is None:
                abort(400, status="error", message="property_id is required")

            # Checking if property_id is instance of the int class.
            if not isinstance(property_id, int):
                abort(400, status="error",
                      message="property_id must be integer")

            # Checking if size is positive.
            if property_id < 0:
                abort(400, status="error",
                      message="property_id must be positive")

            # Creating the new instance.
            new_favorite = Favorite(id, property_id)
            # Adding the new instance to database.
            db.session.add(new_favorite)
            # Commit changes.
            db.session.commit()
            return {"status": "success", "message": ("Favorite added"
                    " successfully")}, 200
        except IntegrityError:
            # Rollback changes.
            db.session.rollback()
            abort(400, status="error",
                  message=("Please make sure that the"
                           " property exists and that user has not already"
                           " saved that property as favorite."))
