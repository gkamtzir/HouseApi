from marshmallow import fields
from flask_marshmallow import Marshmallow
from marshmallow_enum import EnumField
from common.Enumerations import GlassTypeEnum
from models.Shared import db

ma = Marshmallow()


class DoorFrameType(db.Model):
    __tablename__ = "door_frame_type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    glass_type = db.Column(db.Enum(GlassTypeEnum), nullable=False)
    screen = db.Column(db.Boolean, nullable=False)

    # Relationships
    properties = db.relationship("Property", backref="door_frame_type")

    def __init__(self, name, glass_type, screen):
        self.name = name
        self.glass_type = glass_type
        self.screen = screen


class DoorFrameTypeSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    glass_type = EnumField(GlassTypeEnum)
    screen = fields.Boolean(required=True)
