from flask_restful import Resource, abort, request
from models.Comment import Comment, CommentSchema
from models.User import UserSchema
from common.Authentication import fetch_token

comment_schema = CommentSchema()
user_schema = UserSchema()


class SupervisorCommentsReceivedResource(Resource):
    def get(self):
        # Authorize user.
        id, role = fetch_token(request.headers.get("Authorization"))
        if id is not None and not isinstance(id, int):
            abort(401, status="error", message=id)
        if id is None:
            abort(401, status="error",
                  message="You have to log in to access this resource")
        if role == "user":
            abort(401, status="error",
                  message="Only supervisors can use this resource")

        comments = Comment.query.filter_by(supervisor_id=id).all()

        # Match every user id to the corresponding user name.
        comments_user = []
        for comment in comments:
            user_name = user_schema.dump(comment.user).data["name"]
            comment = comment_schema.dump(comment).data
            comment["user_name"] = user_name
            comments_user.append(comment)

        return {"status": "success", "data": comments_user}, 200
