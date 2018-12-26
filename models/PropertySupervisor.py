from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class PropertySupervisor(db.Model):
    __tablename__ = 'property_supervisor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    address = db.Column(db.String(40), nullable=True)
    contact_number = db.Column(db.String(15), nullable=False)
    contact_name = db.Column(db.String(25), nullable=False)
    contact_email = db.Column(db.String(40), nullable=False)
    website = db.Column(db.String(30), nullable=True)

    def __init__(self, name, address, contact_number,
                 contact_name, contact_email, website):
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.contact_name = contact_name
        self.contact_email = contact_email
        self.website = website


class PropertySupervisorSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    address = fields.String(required=False)
    contact_number = fields.String(required=True)
    contact_name = fields.String(required=True)
    contact_email = fields.String(required=True)
    website = fields.String(required=False)
