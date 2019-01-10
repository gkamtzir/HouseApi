from flask import Blueprint
from flask_restful import Api

# Resources.
from resources.User import UserResource
from resources.PropertySupervisor import PropertySupervisorResource
from resources.City import CityResource
from resources.DoorFrameType import DoorFrameTypeResource
from resources.HeatingType import HeatingTypeResource
from resources.Favorite import FavoriteResource
from resources.Comment import CommentResource
from resources.PropertyAction import PropertyActionResource
from resources.Visit import VisitResource
from resources.Property import PropertyResource
from resources.FavoredBy import FavoredByResource
from resources.SupervisorComments import SupervisorCommentsResource
from resources.Login import LoginResource
from resources.UserFavorites import UserFavoritesResource
from resources.Search import SearchResource

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# Routes
api.add_resource(UserResource, "/User")
api.add_resource(PropertySupervisorResource, "/PropertySupervisor")
api.add_resource(CityResource, "/City")
api.add_resource(DoorFrameTypeResource, "/DoorFrameType")
api.add_resource(HeatingTypeResource, "/HeatingType")
api.add_resource(FavoriteResource, "/Favorite")
api.add_resource(CommentResource, "/Comment")
api.add_resource(PropertyActionResource, "/PropertyAction")
api.add_resource(VisitResource, "/Visit")
api.add_resource(PropertyResource, "/Property")
api.add_resource(FavoredByResource, "/FavoredBy/<int:property_id>")
api.add_resource(SupervisorCommentsResource,
                 "/SupervisorComments/<int:supervisor_id>")
api.add_resource(LoginResource, "/Login")
api.add_resource(UserFavoritesResource, "/UserFavorite/<int:user_id>")
api.add_resource(SearchResource, "/Search")
