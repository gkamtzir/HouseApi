from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow_enum import EnumField
from common.Enumerations import PropertyActionEnum

ma = Marshmallow()
db = SQLAlchemy()


class PropertyAction(db.Model):
    __tablename__ = "property_action"
    property_id = db.Column(db.Integer,
                            db.ForeignKey("property.id",
                                          ondelete="CASCADE"),
                            primary_key=True)
    action = db.Column(db.Enum(PropertyActionEnum), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __init__(self, property_id, action, price):
        self.property_id = property_id
        self.action = action
        self.price = price


class PropertyActionSchema(ma.Schema):
    property_id = fields.Integer(dump_only=True)
    action = EnumField(PropertyActionEnum)
    price = fields.Integer(required=True)
