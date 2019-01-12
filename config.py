import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/housedb"

JWT_SECRET_KEY = "THIS_SECRET_KEY_IS_GOING_TO_SELF-DESTRUCT"
