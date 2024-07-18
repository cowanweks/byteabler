import datetime
from uuid import uuid4
from dataclasses import dataclass
from sqlalchemy.types import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .extensions import db


<<<<<<< HEAD
class User(db.Model):
    """Model Representing Users"""
=======
# Model Representing Users
class Users(db.Model):
    staff_no: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    username: Mapped[str] = mapped_column(
        db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(255))
    role = db.Column(db.String(25))
    reg_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
>>>>>>> cbacc08b0b74fe0cbca5be297c545a36cc51f744

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


<<<<<<< HEAD
class Staff(db.Model):
    """Model Representing Staffs"""
=======
# Model Representing Staffs
class Staffs(db.Model):
    staff_no: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String(25), nullable=False)
    middle_name: Mapped[str] = mapped_column(db.String(25), nullable=True)
    last_name: Mapped[str] = mapped_column(db.String(25), nullable=False)
    nat_id = db.Column(db.String(25))
    phone_no = db.Column(db.String(25))
    email = db.Column(db.String(25))
>>>>>>> cbacc08b0b74fe0cbca5be297c545a36cc51f744

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


<<<<<<< HEAD
class ClassRep(db.Model):
    """Model Representing Class Reps"""
=======
# Model Representing Class Reps
class ClassReps(db.Model):
    reg_no: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String(25), nullable=False)
    middle_name: Mapped[str] = mapped_column(db.String(25), nullable=True)
    last_name: Mapped[str] = mapped_column(db.String(25), nullable=False)
    intake = db.Column(db.String(25))
    phone_no = db.Column(db.String(25))
    email = db.Column(db.String(25))
>>>>>>> cbacc08b0b74fe0cbca5be297c545a36cc51f744

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


<<<<<<< HEAD
class Unit(db.Model):
    """Model Representing Units"""
=======
# Model Representing Units
class Units(db.Model):
    unit_code: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    unit_name: Mapped[str] = mapped_column(db.String(25), nullable=False)
>>>>>>> cbacc08b0b74fe0cbca5be297c545a36cc51f744

    unit_code = mapped_column(db.String(25), primary_key=True)
    unit_name = mapped_column(db.String(25), nullable=False)

    def serialize(self):
        return {
            "unitCode": self.unit_code,
            "unitName": self.unit_name,
        }


<<<<<<< HEAD
class Class(db.Model):
    """Model Representing Classes"""
=======
# Model Representing Classes
class Classes(db.Model):
    class_id: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    class_rep: Mapped[str] = mapped_column(db.String(25), nullable=False)
>>>>>>> cbacc08b0b74fe0cbca5be297c545a36cc51f744

    class_id = mapped_column(db.String(25), primary_key=True)
    class_name = mapped_column(db.String, default=str(uuid4()))
    class_rep = mapped_column(db.String(25), nullable=False)

    def serialize(self):
        return {
            "class_id": self.class_id,
            "class_rep": self.class_rep,
        }


<<<<<<< HEAD
class Role(db.Model):
    """Model Representing Roles available to registered users"""
=======
# Model Representing Roles available to registered users
class Roles(db.Model):
    role: Mapped[str] = mapped_column(db.String(25), primary_key=True)
>>>>>>> cbacc08b0b74fe0cbca5be297c545a36cc51f744

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
