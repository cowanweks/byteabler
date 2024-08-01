import time
from enum import Enum
from wtforms import Form, StringField, validators, ValidationError


class Weekdays(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


def validate_weekday(form, field):
    """"""

    if field.data not in Weekdays:
        raise ValidationError("""
        Supported Days are Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday""")


def validate_time(form, field):
    try:
        time.strptime(field.data, '%H:%M')
    except ValueError:
        raise ValidationError('Invalid time format. Supported format is HH:MM')


class LectureRegForm(Form):
    lectureId = StringField("Lecture ID", validators=[])
    classId = StringField("Class ID", validators=[validators.DataRequired("Please input the Class ID!")])
    unitCode = StringField("Unit Code", validators=[validators.DataRequired("Please input the Unit Code!")])
    lecturer = StringField("Lecturer", validators=[validators.DataRequired("Please input the Lecturer!")])
    weekDay = StringField("Weekday", validators=[validators.DataRequired("Please input the Week Day!"),
                                                 validate_weekday])
    startTime = StringField("Start Time", validators=[validators.DataRequired("Please input the Start Time!"),
                                                      validate_time])
    endTime = StringField("End Time", validators=[validators.DataRequired("Please input the End Time!"),
                                                  validate_time])


class LectureUpdateForm(Form):
    ...
