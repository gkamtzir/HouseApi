from marshmallow import fields
from flask_marshmallow import Marshmallow
from models.Shared import db

ma = Marshmallow()


class Favorite(db.Model):
    __tablename__ = "favorite"
    user_id = db.Column(db.Integer,
                        db.ForeignKey("user.id", ondelete="CASCADE"),
                        primary_key=True, nullable=False)
    property_id = db.Column(db.Integer,
                            db.ForeignKey("property.id", ondelete="CASCADE"),
                            primary_key=True, nullable=False)

    def __init__(self, user_id, property_id):
        self.user_id = user_id
        self.property_id = property_id


class FavoriteSchema(ma.Schema):
    user_id = fields.Integer(dump_only=True)
    property_id = fields.Integer(dump_only=True)
