""" """

from uuid import uuid4
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask import Blueprint, request, jsonify
from app.models import db, ClassRep
from app.forms.classrep import ClassRepUpdateForm, ClassRepRegistrationForm


# Role blueprint
class_rep_route = Blueprint(
    "class_rep_route", __name__, url_prefix="/api/v1/classreps"
)


@class_rep_route.route("/", methods=["POST"])
def new():
    """Class Rep Registration Route"""

    form = ClassRepRegistrationForm(request.form)

    if not form.validate():
        return jsonify(form.errors), 400

    try:
        new_class_rep = ClassRep(reg_no=form.regNo.data,
                                 first_name=form.firstName.data,
                                 middle_name=form.middleName.data,
                                 last_name=form.lastName.data,
                                 phone_no=form.mobileNo.data,
                                 email=form.email.data
                                 )
        db.session.add(new_class_rep)

        db.session.commit()
        return jsonify("Successfully added new Class Rep!"), 201

    except IntegrityError:
        return jsonify("Class Rep already exists!"), 409

    except SQLAlchemyError as ex:
        return jsonify(msg="Database error occurred!", error=str(ex)), 500


@class_rep_route.route("/<string:reg_no>", methods=["GET"])
def get(reg_no: str):
    """Route to get Class Representatives"""

    try:
        class_reps = db.session.query(ClassRep).filter_by(reg_no=reg_no).all()

        serialized_class_reps = [class_rep.serialize() for class_rep in class_reps]
        return jsonify(serialized_class_reps), 200

    except SQLAlchemyError as ex:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(ex)), 500


@class_rep_route.route("/", methods=["GET"])
def get_class_reps():
    """Route to get Class Representatives"""

    try:
        class_reps = db.session.query(ClassRep).all()

        serialized_class_reps = [class_rep.serialize() for class_rep in class_reps]
        return jsonify(serialized_class_reps), 200

    except SQLAlchemyError as ex:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(ex)), 500


# The Route that handles classrep information update
@class_rep_route.route("/", methods=["PUT", "PATCH"])
def update():
    """"""
    classrep_id = request.args.get("classrep_id")
    data = request.get_json()

    try:
        db.session.execute(
            db.update(ClassRep)
            .where(ClassRep.classrep_id == classrep_id)
            .values(data)
        )
        db.session.commit()

    except SQLAlchemyError as ex:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(ex)), 500

    return jsonify(msg="Successfully Updated Role!"), 200


# The route that handles classrep deletion
@class_rep_route.route("/", methods=["DELETE"])
def delete():
    """"""
    classrep_id = request.args.get("classrep_id")

    try:
        db.session.execute(
            db.delete(ClassRep).where(ClassRep.classrep_id == classrep_id)
        )
        db.session.commit()
        return jsonify(msg="Successfully Deleted Role!"), 200

    except SQLAlchemyError as ex:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(ex)), 500
