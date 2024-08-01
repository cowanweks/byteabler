import uuid
from flask import Blueprint, request, jsonify, session
from app.models import db, Lecture, Class
from app.forms.lecture import LectureRegForm
import datetime

# Class blueprint
lecture_route = Blueprint("lecture_route", __name__, url_prefix="/api/v1/lectures")


@lecture_route.get("/")
def get_lectures_by_user_route():
    """"""
    staff_no = request.args.get('staffNo')
    reg_no = request.args.get('regNo')
    day = request.args.get('day')

    dt = datetime.datetime.now()
    weekday = dt.strftime("%A")

    if not staff_no and not reg_no:
        #
        try:
            lectures = db.session.query(Lecture).order_by(Lecture.lecture_id).all()

            serialized_lectures = [_lecture.serialize() for _lecture in lectures]
            return jsonify(serialized_lectures), 200

        except Exception as ex:
            print(ex)
            return jsonify(str(ex)), 500

    if staff_no and not reg_no:

        if (day is not None) and (day == 'today'):
            # Fetch today's lectures
            lectures = (db.session.query(Lecture).filter_by(lecturer=staff_no, week_day=weekday)
                        .order_by(Lecture.lecture_id).all())
        else:
            # Fetch All upcoming lectures
            lectures = (db.session.query(Lecture).filter_by(lecturer=staff_no)
                        .order_by(Lecture.lecture_id).all())

        if len(lectures) < 1:
            return jsonify([]), 200

        serialized_lectures = [_lecture.serialize() for _lecture in lectures]
        return jsonify(serialized_lectures), 200

    if reg_no and not staff_no:
        #
        class_id = db.session.query(Class.class_id).filter_by(class_rep=reg_no).scalar()

        if class_id is None:
            return jsonify("Class {} not found".format(class_id))

        if (day is not None) and (day == 'today'):
            print(class_id, weekday)
            lectures = (db.session.query(Lecture).filter_by(class_id=class_id, week_day=weekday)
                        .order_by(Lecture.lecture_id).all())

        else:
            lectures = (db.session.query(Lecture).filter_by(class_id=class_id).order_by(Lecture.lecture_id).all())

        if len(lectures) < 1:
            return jsonify([]), 200

        serialized_lectures = [_lecture.serialize() for _lecture in lectures]
        return jsonify(serialized_lectures), 200


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
