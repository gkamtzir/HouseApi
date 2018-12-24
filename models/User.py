from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)
    contact_email = db.Column(db.String(40), nullable=False)

    def __init__(self, name, contact_number, contact_email):
        self.name = name
        self.contact_number = contact_number
        self.contact_email = contact_email


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    contact_number = fields.String(required=True)
    contact_email = fields.String(required=True)