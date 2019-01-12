from flask_restful import Resource, request, abort
from models.Favorite import Favorite,\
    FavoriteSchema
from common.Authentication import fetch_token

favorites_schema = FavoriteSchema(many=True)


class FavoriteResource(Resource):
    def get(self):
        # Authorize user.
        id, role = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        if id is None:
            abort(401, status="error",
                  message="You have to log in to access this resource")
        favorites = Favorite.query.all()
        favorites = favorites_schema\
            .dump(favorites).data
        return {"status": "success", "data": favorites}, 200
