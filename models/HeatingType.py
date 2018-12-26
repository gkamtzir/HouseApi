from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow_enum import EnumField
from common.Enumerations import HeatingTypeEnum

ma = Marshmallow()
db = SQLAlchemy()


class HeatingType(db.Model):
    __tablename__ = "heating_type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    type = db.Column(db.Enum(HeatingTypeEnum), nullable=False)

    def __init__(self, name, type):
        self.name = name
        self.type = type


class HeatingTypeSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    type = EnumField(HeatingTypeEnum)
