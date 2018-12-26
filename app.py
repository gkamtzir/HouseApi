from flask import Blueprint
from flask_restful import Api

# Resources.
from resources.User import UserResource
from resources.PropertySupervisor import PropertySupervisorResource
from resources.City import CityResource
from resources.DoorFrameType import DoorFrameTypeResource
from resources.HeatingType import HeatingTypeResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(UserResource, "/User")
api.add_resource(PropertySupervisorResource, "/PropertySupervisor")
api.add_resource(CityResource, "/City")
api.add_resource(DoorFrameTypeResource, "/DoorFrameType")
api.add_resource(HeatingTypeResource, "/HeatingType")
