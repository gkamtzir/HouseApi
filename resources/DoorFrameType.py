from flask_restful import Resource, request, abort
from models.DoorFrameType import DoorFrameType,\
    DoorFrameTypeSchema
from common.Authentication import fetch_token

door_frame_types_schema = DoorFrameTypeSchema(many=True)


class DoorFrameTypeResource(Resource):
    def get(self):
        # Authorize user.
        id, role = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        door_frame_types = DoorFrameType.query.all()
        door_frame_types = door_frame_types_schema\
            .dump(door_frame_types).data
        return {"status": "success", "data": door_frame_types}, 200
