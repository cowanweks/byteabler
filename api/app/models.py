import datetime
from uuid import uuid4
from dataclasses import dataclass
from sqlalchemy.types import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .extensions import db


class User(db.Model):
    """Model Representing Users"""

    user_id = mapped_column(db.String, primary_key=True)
    staff_no = mapped_column(db.String(25), unique=True)
    username = mapped_column(db.String(25), unique=True, nullable=False)
    password = mapped_column(db.String(255))
    roles = mapped_column(db.String(25))
    reg_date = mapped_column(
        DateTime(timezone=True), default=datetime.datetime.now()
    )

    def serialize(self):
        return {
            "user_id": self.user_id,
            "staff_no": self.staff_no,
            "password": self.password,
            "username": self.username,
            "role": self.roles,
            "registration_date": self.reg_date,
        }


class Staff(db.Model):
    """Model Representing Staffs"""

    staff_no = mapped_column(db.String(25), primary_key=True, default=str(uuid4()))
    first_name = mapped_column(db.String(25), nullable=False)
    middle_name = mapped_column(db.String(25), nullable=True)
    last_name = mapped_column(db.String(25), nullable=False)
    nat_id = mapped_column(db.String(25))
    phone_no = mapped_column(db.String(25))
    email = mapped_column(db.String(25))

    def serialize(self):
        return {
            "staff_no": self.staff_no,
            "firstname": self.first_name,
            "middlename": self.middle_name,
            "lastname": self.last_name,
            "nationalID": self.nat_id,
            "phone": self.phone_no,
            "email": self.email,
        }


class ClassRep(db.Model):
    """Model Representing Class Reps"""

    classrep_id = mapped_column(db.String, primary_key=True, default=str(uuid4()))
    reg_no = mapped_column(db.String(25))
    firstname = mapped_column(db.String(25), nullable=False)
    middlename = mapped_column(db.String(25), nullable=True)
    lastname = mapped_column(db.String(25), nullable=False)
    class_id = mapped_column(db.String(25), nullable=False)
    phoneno = mapped_column(db.String(25), nullable=False)
    email = mapped_column(db.String(25), nullable=False)

    def serialize(self):
        return {
            "classrep_id": self.classrep_id,
            "reg_no": self.reg_no,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "class_id": self.class_id,
            "phone": self.phoneno,
            "email": self.email,
        }


class Unit(db.Model):
    """Model Representing Units"""

    unit_code = mapped_column(db.String(25), primary_key=True)
    unit_name = mapped_column(db.String(25), nullable=False)

    def serialize(self):
        return {
            "unitCode": self.unit_code,
            "unitName": self.unit_name,
        }


class Class(db.Model):
    """Model Representing Classes"""

    class_id = mapped_column(db.String(25), primary_key=True)
    class_name = mapped_column(db.String, default=str(uuid4()))
    class_rep = mapped_column(db.String(25), nullable=False)

    def serialize(self):
        return {
            "class_id": self.class_id,
            "class_rep": self.class_rep,
        }


class Role(db.Model):
    """Model Representing Roles available to registered users"""

    role_id = mapped_column(
        db.String(25), primary_key=True, nullable=False,
        default=str(uuid4())
    )
    role_name = mapped_column(db.String(25), unique=True, nullable=False)
    role_description = mapped_column(db.String(255))

    def serialize(self):
        return {
            "role_id": self.role_id,
            "role_name": self.role_name,
        }
