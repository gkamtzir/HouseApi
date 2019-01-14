from flask_restful import Resource, request
from models.PropertySupervisor import PropertySupervisor, \
    PropertySupervisorSchema
from common.Authentication import encode_auth_token

property_supervisor_schema = PropertySupervisorSchema()


class LoginSupervisorResource(Resource):
    def post(self):
        post_data = request.get_json()
        try:
            supervisor = PropertySupervisor.query.\
                filter_by(contact_email=post_data.get("email")).first()
            if supervisor is None:
                return {"status": "Fail", "message": ("Supervisor does not"
                                                      " exist.")}, 404
            else:
                supervisor = property_supervisor_schema.dump(supervisor).data
                # Generate token.
                token = str(encode_auth_token(supervisor["id"], "supervisor"))
                # Removed token quotes.
                token = token[2:len(token) - 1]
                return {"status": "success",
                        "token": token}, 200
        except Exception as e:
            print(e)
            return {"status": "Fail", "message": "Try again"}, 500
