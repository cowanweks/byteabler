import datetime
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column
from .extensions import db


# Model Representing Users
@dataclass
class Users(db.Model):
    staff_no: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    username: Mapped[str] = mapped_column(
        db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(255))
    role: Mapped[str] = mapped_column(db.String(25))
    reg_date: Mapped[datetime] = mapped_column(
        db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return """
        StaffNo: {},
        UserName: {},
        Role: {},
        RegistrationDate: {}
        """.format(self.staff_no, self.username, self.role, self.reg_date)


# TODO Model Representing Staffs
@dataclass
class Staffs(db.Model):
    staff_no: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String(25), nullable=False)
    middle_name: Mapped[str] = mapped_column(db.String(25), nullable=True)
    last_name: Mapped[str] = mapped_column(db.String(25), nullable=False)
    nat_id = db.Column(db.String(25))
    phone_no = db.Column(db.String(25))
    email = db.Column(db.String(25))

    def __repr__(self):
        return """
        StaffNo: {},
        FastName: {},
        MiddName: {},
        LastName: {},
        NatID No: {},
        Mobile Phone: {},
        Email: {}
        """.format(self.staff_no, self.first_name, self.middle_name, self.last_name, self.nat_id, self.phone_no, self.email)


# TODO Model Representing Class Reps
@dataclass
class ClassReps(db.Model):
    reg_no: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    firstname: Mapped[str] = mapped_column(db.String(25), nullable=False)
    middlename: Mapped[str] = mapped_column(db.String(25), nullable=True)
    lastname: Mapped[str] = mapped_column(db.String(25), nullable=False)
    class_id = db.Column(db.String(25))
    phoneno = db.Column(db.String(25))
    email = db.Column(db.String(25))

    def __repr__(self):
        return """
        RegNo: {},
        FirstName: {},
        MiddName: {},
        LastName: {},
        Class: {},
        Mobile Phone: {},
        Email: {}
        """.format(self.reg_no, self.firstname, self.middlename, self.lastname, self.class_id, self.phoneno, self.email)


# Model Representing Units
@dataclass
class Units(db.Model):
    unit_code: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    unit_name: Mapped[str] = mapped_column(db.String(25), nullable=False)

    def __repr__(self):
        return """
        Unit Code: {},
        Unit Name: {},
        """.format(self.unit_code, self.unit_name)


# Model Representing Classes
@dataclass
class Classes(db.Model):
    class_id: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    class_rep: Mapped[str] = mapped_column(db.String(25), nullable=False)

    def __repr__(self):
        return """
        Class ID: {},
        Class Representative: {},
        """.format(self.class_id, self.class_rep)


# Model Representing Roles available to registered users
@dataclass
class Roles(db.Model):
    role_id: Mapped[str] = mapped_column(db.String(25), primary_key=True)
    role_name: Mapped[str] = mapped_column(db.String(25))

    def __repr__(self) -> str:
        return """
        RoleID: {},
        RoleName: {}
        """.format(self.role_id, self.role_name)
