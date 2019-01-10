from flask import current_app as app
import jwt
import datetime


def encode_auth_token(user_id):
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(
                days=1,
                seconds=0),
            "iat": datetime.datetime.utcnow(),
            "sub": user_id
        }
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


def fetch_token(authorization):
    # Fetching token.
    token = authorization.split(" ")[1]
    # Decoding token to get user's id.
    return decode_auth_token(token)
