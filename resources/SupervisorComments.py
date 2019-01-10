from flask_restful import Resource, abort
from models.PropertySupervisor import PropertySupervisor
from models.Comment import Comment, CommentSchema
from models.User import UserSchema

comment_schema = CommentSchema()
user_schema = UserSchema()


class SupervisorCommentsResource(Resource):
    def get(self, supervisor_id):
        supervisor = PropertySupervisor.query.filter_by(id=supervisor_id)\
            .first()
        if supervisor is None:
            abort(404, message="Supervisor with id = {} doesn't exist"
                  .format(supervisor_id))
        comments = Comment.query.filter_by(supervisor_id=supervisor.id).all()

        # Match every user id to the corresponding user name.
        comments_user = []
        for comment in comments:
            user_name = user_schema.dump(comment.user).data["name"]
            comment = comment_schema.dump(comment).data
            comment["user_name"] = user_name
            comments_user.append(comment)

        return {"status": "success", "data": comments_user}, 200
