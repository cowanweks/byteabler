from .flask_init import flask_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# postgres://cowanweks:ultimate@localhost:5432/timetabler

# Setup the database uri
flask_app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://arekings:arekings@localhost/timetabler"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(app=flask_app, model_class=Base)
