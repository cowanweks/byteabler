import datetime
from sqlalchemy.orm import Mapped, mapped_column
from .db_config import flask_app, db


# Model Representing Users
class Users(db.Model):
    staff_no: Mapped[str] = mapped_column(db.String, primary_key=True)
    username: Mapped[str] = mapped_column(
        db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    role = db.Column(db.String)
    reg_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return """
        StaffNo: {},
        UserName: {},
        Role: {},
        RegistrationDate: {}
        """.format(self.staff_no, self.username, self.role, self.reg_date)


# Model Representing Staffs
class Staffs(db.Model):
    staff_no: Mapped[str] = mapped_column(db.String, primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String, nullable=False)
    middle_name: Mapped[str] = mapped_column(db.String, nullable=True)
    last_name: Mapped[str] = mapped_column(db.String, nullable=False)
    nat_id = db.Column(db.String)
    phone_no = db.Column(db.String)
    email = db.Column(db.String)

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


# Model Representing Class Reps
class ClassReps(db.Model):
    reg_no: Mapped[str] = mapped_column(db.String, primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String, nullable=False)
    middle_name: Mapped[str] = mapped_column(db.String, nullable=True)
    last_name: Mapped[str] = mapped_column(db.String, nullable=False)
    intake = db.Column(db.String)
    phone_no = db.Column(db.String)
    email = db.Column(db.String)

    def __repr__(self):
        return """
        RegNo: {},
        FirstName: {},
        MiddName: {},
        LastName: {},
        Class: {},
        Mobile Phone: {},
        Email: {}
        """.format(self.staff_no, self.first_name, self.middle_name, self.last_name, self.intake, self.phone_no, self.email)


# Model Representing Units
class Units(db.Model):
    unit_code: Mapped[str] = mapped_column(db.String, primary_key=True)
    unit_name: Mapped[str] = mapped_column(db.String, nullable=False)

    def __repr__(self):
        return """
        Unit Code: {},
        Unit Name: {},
        """.format(self.unit_code, self.unit_name)


# Model Representing Classes
class Classes(db.Model):
    class_id: Mapped[str] = mapped_column(db.String, primary_key=True)
    class_rep: Mapped[str] = mapped_column(db.String, nullable=False)

    def __repr__(self):
        return """
        Class ID: {},
        Class Representative: {},
        """.format(self.class_id, self.class_rep)


# Model Representing Roles available to registered users
class Roles(db.Model):
    role: Mapped[str] = mapped_column(db.String, primary_key=True)

    def __repr__(self) -> str:
        return """
        Role: {}
        """.format(self.role)


# Create all the Tables from the above models
with flask_app.app_context():
    db.create_all()
