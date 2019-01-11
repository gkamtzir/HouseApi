from flask_restful import Resource, abort, request
from sqlalchemy.exc import IntegrityError
from models.Favorite import Favorite
from models.User import UserSchema
from models.Shared import db
from common.Authentication import fetch_token

user_schema = UserSchema()


class AddFavoriteResource(Resource):
    def get(self, property_id):
        try:
            # Authorize user.
            id, role = fetch_token(request.headers.get("Authorization"))
            if id is not None and not isinstance(id, int):
                abort(401, status="error", message=id)
            if role == "supervisor":
                abort(401, status="error",
                      message="Only users can use this resource")

            # Creating the new instance.
            new_favorite = Favorite(1, property_id)
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
