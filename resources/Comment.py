from flask_restful import Resource, request, abort
from models.Comment import Comment,\
    CommentSchema
from common.Authentication import fetch_token

comments_schema = CommentSchema(many=True)


class CommentResource(Resource):
    def get(self):
        # Authorize user.
        id, role = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        if id is None:
            abort(401, status="error",
                  message="You have to log in to access this resource")
        comments = Comment.query.all()
        comments = comments_schema\
            .dump(comments).data
        return {"status": "success", "data": comments}, 200
