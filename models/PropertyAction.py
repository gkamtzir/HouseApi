from marshmallow import fields
from flask_marshmallow import Marshmallow
from marshmallow_enum import EnumField
from common.Enumerations import PropertyActionEnum
from models.Shared import db

ma = Marshmallow()


class PropertyAction(db.Model):
    __tablename__ = "property_action"
    property_id = db.Column(db.Integer,
                            db.ForeignKey("property.id",
                                          ondelete="CASCADE"),
                            primary_key=True)
    action = db.Column(db.Enum(PropertyActionEnum), nullable=False,
                       primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    def __init__(self, property_id, action, price):
        self.property_id = property_id
        self.action = action
        self.price = price


class PropertyActionSchema(ma.Schema):
    property_id = fields.Integer(dump_only=True)
    action = EnumField(PropertyActionEnum)
    price = fields.Integer(required=True)


class PropertyActionShortSchema(ma.Schema):
    action = EnumField(PropertyActionEnum)
    price = fields.Integer(required=True)