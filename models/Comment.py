from marshmallow import fields
from flask_marshmallow import Marshmallow
from models.Shared import db

ma = Marshmallow()


class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey("user.id", ondelete="CASCADE"),
                        nullable=False)
    supervisor_id = db.Column(db.Integer,
                              db.ForeignKey("property_supervisor.id",
                                            ondelete="CASCADE"),
                              nullable=False)
    comment = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    # Relationships.
    user = db.relationship("User", backref="comment")

    def __init__(self, user_id, supervisor_id, comment, rating):
        self.user_id = user_id
        self.supervisor_id = supervisor_id
        self.comment = comment
        self.rating = rating


class CommentSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)
    user_name = fields.String(required=False)
    supervisor_id = fields.Integer(required=True)
    comment = fields.String(required=True)
    rating = fields.Integer(required=True)