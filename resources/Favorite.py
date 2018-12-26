from flask_restful import Resource
from models.Favorite import Favorite,\
    FavoriteSchema

favorites_schema = FavoriteSchema(many=True)
favorite_schema = FavoriteSchema()


class FavoriteResource(Resource):
    def get(self):
        favorites = Favorite.query.all()
        favorites = favorites_schema\
            .dump(favorites).data
        return {"status": "success", "data": favorites}, 200
