from marshmallow import fields
from flask_marshmallow import Marshmallow
from models.Shared import db

ma = Marshmallow()


class City(db.Model):
    __tablename__ = "city"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    country_name = db.Column(db.String(25), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    average_temp = db.Column(db.Numeric(3, 1), nullable=False)
    average_humidity = db.Column(db.Integer, nullable=False)
    average_precip = db.Column(db.Numeric(5, 1), nullable=False)

    # Relationships
    properties = db.relationship("Property", backref="city")

    def __init__(self, name, country_name, population, average_temp,
                 average_humidity, average_precip):
        self.name = name
        self.country_name = country_name
        self.population = population
        self.average_temp = average_temp
        self.average_humidity = average_humidity
        self.average_precip = average_precip


class CitySchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    country_name = fields.String(required=True)
    population = fields.Integer(required=True)
    average_temp = fields.Float(required=True)
    average_humidity = fields.Integer(required=True)
    average_precip = fields.Float(required=True)
