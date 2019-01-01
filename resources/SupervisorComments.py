from flask_restful import Resource, abort
from models.PropertySupervisor import PropertySupervisor
from models.Comment import Comment, CommentSchema

comments_schema = CommentSchema(many=True)


class SupervisorCommentsResource(Resource):
    def get(self, supervisor_id):
        supervisor = PropertySupervisor.query.filter_by(id=supervisor_id)\
            .first()
        if supervisor is None:
            abort(404, message="Supervisor with id = {} doesn't exist"
                  .format(supervisor_id))
        comments = Comment.query.filter_by(supervisor_id=supervisor.id).all()
        comments = comments_schema.dump(comments).data

        return {"status": "success", "data": comments}, 200
