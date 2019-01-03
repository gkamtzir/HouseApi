from flask_restful import Resource
from models.DoorFrameType import DoorFrameType,\
    DoorFrameTypeSchema

door_frame_types_schema = DoorFrameTypeSchema(many=True)


class DoorFrameTypeResource(Resource):
    def get(self):
        door_frame_types = DoorFrameType.query.all()
        door_frame_types = door_frame_types_schema\
            .dump(door_frame_types).data
        return {"status": "success", "data": door_frame_types}, 200
