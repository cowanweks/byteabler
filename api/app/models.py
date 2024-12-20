import datetime
from sqlalchemy import ForeignKey, String, DateTime, Time
from sqlalchemy.orm import mapped_column, Mapped, relationship
from .extensions import db


class User(db.Model):
    """Model Representing Users"""
    __tablename__ = "users"

    user_id = mapped_column(String, primary_key=True)
    username = mapped_column(String(25), unique=True, nullable=False)
    password = mapped_column(String(255))
    roles = mapped_column(String(25))
    reg_date = mapped_column(DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = mapped_column(DateTime(timezone=True), default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def serialize(self):
        return {
            "userId": self.user_id,
            "password": self.password,
            "userName": self.username,
            "roles": self.roles,
            "regDate": self.reg_date
        }


class Staff(db.Model):
    """Model Representing Staffs"""
    __tablename__ = "staffs"

    staff_no = mapped_column(String(25), primary_key=True)
    first_name = mapped_column(String(25), nullable=False)
    middle_name = mapped_column(String(25), nullable=True)
    last_name = mapped_column(String(25), nullable=False)
    nat_id = mapped_column(String(25))
    phone_no = mapped_column(String(25))
    email = mapped_column(String(25))
    reg_date = mapped_column(DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = mapped_column(DateTime(timezone=True), default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def serialize(self):
        return {
            "staffNo": self.staff_no,
            "firstName": self.first_name,
            "middleName": self.middle_name,
            "lastName": self.last_name,
            "natId": self.nat_id,
            "phone": self.phone_no,
            "email": self.email,
        }


class Unit(db.Model):
    """Model Representing Units"""
    __tablename__ = "units"

    unit_code = mapped_column(String(25), primary_key=True)
    unit_name = mapped_column(String(25), nullable=False)
    reg_date = mapped_column(DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = mapped_column(DateTime(timezone=True), default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def serialize(self):
        return {
            "unitCode": self.unit_code,
            "unitName": self.unit_name,
        }


class Class(db.Model):
    """Model Representing Classes"""
    __tablename__ = "classes"

    class_id = mapped_column(String(25), primary_key=True)
    class_rep = mapped_column(String, nullable=False)
    reg_date = mapped_column(DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = mapped_column(DateTime(timezone=True), default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    # class_rep = relationship('ClassRep', backref="classes", uselist=False)

    def serialize(self):
        return {
            "classId": self.class_id,
            "classRep": self.class_rep
        }


class ClassRep(db.Model):
    """Model Representing Class Reps"""
    __tablename__ = "class_reps"

    reg_no = mapped_column(String(25), primary_key=True)
    class_id = mapped_column(String,
                             ForeignKey("classes.class_id", onupdate="CASCADE", ondelete="CASCADE"))
    first_name = mapped_column(String(25), nullable=False)
    middle_name = mapped_column(String(25), nullable=True)
    last_name = mapped_column(String(25), nullable=False)
    phone_no = mapped_column(String(25), nullable=False)
    email = mapped_column(String(25), nullable=False)
    reg_date = mapped_column(DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = mapped_column(DateTime(timezone=True), default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def serialize(self):
        return {
            "regNo": self.reg_no,
            "firstName": self.first_name,
            "middleName": self.middle_name,
            "lastName": self.last_name,
            "mobileNo": self.phone_no,
            "email": self.email,
        }


class Role(db.Model):
    """Model Representing Roles available to registered users"""
    __tablename__ = "roles"

    role_id = mapped_column(String(25), primary_key=True)
    role_name = mapped_column(String(25), unique=True, nullable=False)
    role_description = mapped_column(String(255))
    reg_date = mapped_column(DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = mapped_column(DateTime(timezone=True), default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def serialize(self):
        return {
            "roleId": self.role_id,
            "roleName": self.role_name,
        }


class UnitAssignment(db.Model):
    """Model Representing a Unit"""
    __tablename__ = "unit_assignment"

    assignment_id = mapped_column(String, primary_key=True)
    class_id = mapped_column(ForeignKey("classes.class_id"))
    unit_id = mapped_column(ForeignKey("units.unit_code"))
    lecturer = mapped_column(ForeignKey("staffs.staff_no"))
    reg_date = mapped_column(DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = mapped_column(DateTime(timezone=True), default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    # assigned_unit: Mapped["Unit"] = relationship(back_populates="assigned_unit")
    # assigned_class: Mapped["Class"] = relationship(back_populates="assigned_class")
    # assigned_lecturer: Mapped["Staff"] = relationship(back_populates="assigned_lecturer")

    def serialize(self):
        return {
            "assignment_id": self.assignment_id
        }


class Lecture(db.Model):
    """Model Representing every day lectures"""
    __tablename__ = "lectures"

    lecture_id = mapped_column(String, primary_key=True)
    class_id = mapped_column(String, ForeignKey("classes.class_id"))
    unit_code = mapped_column(String, nullable=False)
    lecturer = mapped_column(String, ForeignKey("staffs.staff_no"), nullable=False)
    week_day = mapped_column(String, nullable=False)
    start_time = mapped_column(String, nullable=False)
    end_time = mapped_column(String, nullable=False)
    reg_date = mapped_column(DateTime(timezone=True), default=datetime.datetime.now())
    updated_at = mapped_column(DateTime(timezone=True), default=datetime.datetime.now(),
                               onupdate=datetime.datetime.now())

    # assigned_lecturer: Mapped["Staff"] = relationship(back_populates="assigned_lecturer")

    def serialize(self):

        return {
            "lectureId": self.lecture_id,
            "classId": self.class_id,
            "unitCode": self.unit_code,
            "unitName": db.session.query(Unit.unit_name).filter_by(unit_code=self.unit_code).scalar(),
            "lecturer": self.lecturer,
            "lecName": db.session.query(Staff.first_name).filter_by(staff_no=self.lecturer).scalar(),
            "weekDay": self.week_day,
            "startTime": self.start_time,
            "endTime": self.end_time
        }
