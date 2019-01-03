from flask import current_app as app
import jwt
import datetime


def encode_auth_token(user_id):
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(
                days=0,
                seconds=5),
            "iat": datetime.datetime.utcnow(),
            "sub": user_id
        }
        print(app.config.get("JWT_SECRET_KEY"))
        return jwt.encode(
            payload,
            app.config.get("JWT_SECRET_KEY"),
            algorithm="HS256"
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, app.config.get("JWT_SECRET_KEY"))
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return "Signature expired. Please log in again."
    except jwt.InvalidTokenError:
        return "Invalid token. Please log in again."
