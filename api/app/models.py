import datetime
from dataclasses import dataclass
from sqlalchemy.types import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .extensions import db


@dataclass
class Users(db.Model):
    """Model Representing Users"""

    user_id: Mapped[str] = mapped_column(db.String, primary_key=True)
    staff_no: Mapped[str] = mapped_column(db.String(25), unique=True)
    username: Mapped[str] = mapped_column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(255))
    role: Mapped[str] = mapped_column(db.String(25))
    reg_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.datetime.now()
    )

    def serialize(self):
        return {
            "user_id": self.user_id,
            "staff_no": self.staff_no,
            "password": self.password,
            "username": self.username,
            "role": self.role,
            "registration_date": self.reg_date,
        }


@dataclass
class Staffs(db.Model):
    """Model Representing Staffs"""

    staff_no: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String(25), nullable=False)
    middle_name: Mapped[str] = mapped_column(db.String(25), nullable=True)
    last_name: Mapped[str] = mapped_column(db.String(25), nullable=False)
    nat_id = db.Column(db.String(25))
    phone_no = db.Column(db.String(25))
    email = db.Column(db.String(25))

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


@dataclass
class ClassReps(db.Model):
    """Model Representing Class Reps"""

    classrep_id: Mapped[str] = mapped_column(db.String, primary_key=True)
    reg_no: Mapped[str] = mapped_column(db.String(25))
    firstname: Mapped[str] = mapped_column(db.String(25), nullable=False)
    middlename: Mapped[str] = mapped_column(db.String(25), nullable=True)
    lastname: Mapped[str] = mapped_column(db.String(25), nullable=False)
    class_id: Mapped[str] = mapped_column(db.String(25), nullable=False)
    phoneno: Mapped[str] = mapped_column(db.String(25), nullable=False)
    email: Mapped[str] = mapped_column(db.String(25), nullable=False)

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


@dataclass
class Units(db.Model):
    """Model Representing Units"""

    unit_id: Mapped[str] = mapped_column(db.String, primary_key=True)
    unit_code: Mapped[str] = mapped_column(db.String(25))
    unit_name: Mapped[str] = mapped_column(db.String(25), nullable=False)

    def serialize(self):
        return {
            "unit_id": self.unit_id,
            "unit_code": self.unit_code,
            "unit_name": self.unit_name,
        }


@dataclass
class Classes(db.Model):
    """Model Representing Classes"""

    class_id: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    class_rep: Mapped[str] = mapped_column(db.String(25), nullable=False)

    def serialize(self):
        return {
            "class_id": self.class_id,
            "class_rep": self.class_rep,
        }


@dataclass
class Roles(db.Model):
    """Model Representing Roles available to registered users"""

    role_id: Mapped[str] = mapped_column(
        db.String(25), primary_key=True, nullable=False
    )
    role_name: Mapped[str] = mapped_column(db.String(25), unique=True, nullable=False)
    role_description: Mapped[str] = mapped_column(db.String(255))

    def serialize(self):
        return {
            "role_id": self.role_id,
            "role_name": self.role_name,
        }
