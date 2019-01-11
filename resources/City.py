from flask_restful import Resource, request, abort
from models.City import City,\
    CitySchema
from common.Authentication import fetch_token

cities_schema = CitySchema(many=True)


class CityResource(Resource):
    def get(self):
        # Authorize user.
        id, role = fetch_token(request.headers.get("Authorization"))
        print(id)
        print(role)
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        cities = City.query.all()
        cities = cities_schema\
            .dump(cities).data
        return {"status": "success", "data": cities}, 200
