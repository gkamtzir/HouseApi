from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow_enum import EnumField
from common.Enumerations import VisitStatusEnum

ma = Marshmallow()
db = SQLAlchemy()


class Visit(db.Model):
    __tablename__ = "visit"
    user_id = db.Column(db.Integer,
                        db.ForeignKey("user.id", ondelete="CASCADE"),
                        primary_key=True, nullable=False)
    property_id = db.Column(db.Integer,
                            db.ForeignKey("property.id", ondelete="CASCADE"),
                            primary_key=True, nullable=False)
    visit_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum(VisitStatusEnum), nullable=False)

    def __init__(self, user_id, property_id, visit_date, status):
        self.user_id = user_id
        self.property_id = property_id
        self.visit_date = visit_date
        self.status = status


class VisitSchema(ma.Schema):
    user_id = fields.Integer(dump_only=True)
    property_id = fields.Integer(dump_only=True)
    visit_date = fields.Date(required=True)
    status = EnumField(VisitStatusEnum)
