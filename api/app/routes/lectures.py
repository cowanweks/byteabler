import uuid
import sqlalchemy
from flask import Blueprint, request, jsonify
from app.models import db, Lecture
from app.forms.lecture import LectureRegForm

# Class blueprint
lecture_route = Blueprint("lecture_route", __name__, url_prefix="/api/v1/lectures")


@lecture_route.get("/")
def get_lectures_route():
    """"""

    try:
        lectures = db.session.query(Lecture).order_by(Lecture.lecture_id).all()

        serialized_lectures = [lecture.serialize() for lecture in lectures]
        return jsonify(serialized_lectures), 200

    except Exception as ex:
        print(ex)
        return jsonify(str(ex)), 500


@lecture_route.post("/")
def new():
    """"""
    form = LectureRegForm(request.form)

    try:
        if not form.validate():
            return jsonify(form.errors), 400

        lecture = Lecture(lecture_id=str(uuid.uuid4()), class_id=form.classId.data, unit_code=form.unitCode.data,
                          lecturer=form.lecturer.data, week_day=form.weekDay.data, time=form.time.data)

        db.session.add(lecture)
        db.session.commit()
        return jsonify("Lecture added Successfully!"), 201

    except Exception as ex:
        print(ex)
        return jsonify(str(ex)), 500
