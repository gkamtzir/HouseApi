from flask_restful import Resource
from models.Comment import Comment,\
    CommentSchema

comments_schema = CommentSchema(many=True)


class CommentResource(Resource):
    def get(self):
        comments = Comment.query.all()
        comments = comments_schema\
            .dump(comments).data
        return {"status": "success", "data": comments}, 200
