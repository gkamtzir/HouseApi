from flask_restful import Resource
from models.City import City,\
    CitySchema

cities_schema = CitySchema(many=True)


class CityResource(Resource):
    def get(self):
        cities = City.query.all()
        cities = cities_schema\
            .dump(cities).data
        return {"status": "success", "data": cities}, 200
