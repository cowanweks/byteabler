from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


sess = Session()
jwt = JWTManager()
db = SQLAlchemy(model_class=Base)
