from flask import Blueprint
from flask_restful import Api
from resources.User import UserResource
from resources.PropertySupervisor import PropertySupervisorResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(UserResource, '/User')
api.add_resource(PropertySupervisorResource, '/PropertySupervisor')
