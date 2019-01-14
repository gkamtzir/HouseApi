from marshmallow import fields
from flask_marshmallow import Marshmallow
from marshmallow_enum import EnumField
from common.Enumerations import VisitStatusEnum
from models.Shared import db
from models.Property import PropertySchema

ma = Marshmallow()


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

    # Relationships.
    property = db.relationship("Property", backref="visit")

    def __init__(self, user_id, property_id, visit_date, status):
        self.user_id = user_id
        self.property_id = property_id
        self.visit_date = visit_date
        self.status = status


class VisitSchema(ma.Schema):
    user_id = fields.Integer(dump_only=True)
    visit_date = fields.Date(required=True)
    status = EnumField(VisitStatusEnum)
    property = fields.Nested(PropertySchema)
