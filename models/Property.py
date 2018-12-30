from marshmallow import fields
from flask_marshmallow import Marshmallow
from marshmallow_enum import EnumField
from common.Enumerations import PropertyTypeEnum, EnergyCertificateEnum
from models.Shared import db

ma = Marshmallow()


class Property(db.Model):
    __tablename__ = "property"
    id = db.Column(db.Integer, primary_key=True)
    floor = db.Column(db.Integer, nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)
    street_address = db.Column(db.String(35), nullable=False)
    street_number = db.Column(db.Integer, nullable=True)
    property_type = db.Column(db.Enum(PropertyTypeEnum), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    rooms = db.Column(db.Integer, nullable=True)
    longitude = db.Column(db.Numeric(8, 5), nullable=False)
    latitude = db.Column(db.Numeric(8, 5), nullable=False)
    energy_certificate = db.Column(db.Enum(EnergyCertificateEnum),
                                   nullable=True)
    city_id = db.Column(db.Integer, db.ForeignKey("city.id"), nullable=False)
    supervisor_id = db.Column(db.Integer,
                              db.ForeignKey("property_supervisor.id"),
                              nullable=False)
    heating_type_id = db.Column(db.Integer, db.ForeignKey("heating_type.id"),
                                nullable=False)
    door_frame_id = db.Column(db.Integer, db.ForeignKey("door_frame_type.id"),
                              nullable=False)
    details = db.Column(db.String(150), nullable=True)

    # Relationships
    actions = db.relationship("PropertyAction", backref="property")

    def __init__(self, floor, postal_code, street_address, street_number,
                 property_type, size, rooms, longitude, latitude,
                 energy_certificate, city_id, supervisor_id, heating_type_id,
                 door_frame_id, details):
        self.floor = floor
        self.postal_code = postal_code
        self.street_address = street_address
        self.street_number = street_number
        self.property_type = property_type
        self.size = size
        self.rooms = rooms
        self.longitude = longitude
        self.latitude = latitude
        self.energy_certificate = energy_certificate
        self.city_id = city_id
        self.supervisor_id = supervisor_id
        self.heating_type_id = heating_type_id
        self.door_frame_id = door_frame_id
        self.details = details


class PropertySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    floor = fields.Integer(required=True)
    postal_code = fields.String(required=True)
    street_address = fields.String(required=True)
    street_number = fields.String(required=False)
    property_type = EnumField(PropertyTypeEnum)
    size = fields.Integer(required=True)
    rooms = fields.Integer(required=False)
    longitude = fields.Float(required=True)
    latitude = fields.Float(required=True)
    energy_certificate = EnumField(EnergyCertificateEnum)
    city_id = fields.Integer(required=True)
    supervisor_id = fields.Integer(required=True)
    heating_type_id = fields.Integer(required=True)
    door_frame_id = fields.Integer(required=True)
    details = fields.String(required=False)
