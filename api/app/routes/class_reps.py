""" """

from uuid import uuid4
from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, request, jsonify
from app.models import db, ClassRep


# Role blueprint
classrep_route = Blueprint(
    "classrep_route", __name__, url_prefix="/api/v1/classreps"
)


@classrep_route.route("/", methods=["GET"])
def get_classreps():
    """"""
    classrep_id = request.args.get("classrep_id")

    try:
        if classrep_id:
            classreps = (
                db.session.execute(
                    db.select(ClassRep)
                    .where(ClassRep.classrep_id == classrep_id)
                    .order_by(ClassRep.classrep_id)
                )
                .scalars()
                .all()
            )

        classreps = (
            db.session.execute(db.select(ClassRep).order_by(ClassRep.classrep_id))
            .scalars()
            .all()
        )
        serialized_classreps = [classrep.serialize() for classrep in classreps]
        return jsonify(serialized_classreps), 200

    except SQLAlchemyError as ex:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(ex)), 500


@classrep_route.route("/", methods=["POST"])
def new_classrep():
    """Class Rep Registration endpoint"""

    # TODO Form Validation
    data = request.get_json()

    classrep_id = str(uuid4())
    reg_no = data.get("reg_no")
    class_id = data.get("class_id")
    firstname = data.get("firstname")
    middlename = data.get("middlename")
    lastname = data.get("lastname")
    email = data.get("email")
    phoneno = data.get("phoneno")

    try:
        db.session.add(
            ClassRep(
                reg_no=reg_no,
                class_id=class_id,
                classrep_id=classrep_id,
                firstname=firstname,
                middlename=middlename,
                lastname=lastname,
                email=email,
                phoneno=phoneno,
            )
        )
        db.session.commit()
        return jsonify("Successfully Created new Role!"), 201

    except SQLAlchemyError as ex:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(ex)), 500


# The Route that handles classrep information update
@classrep_route.route("/", methods=["PUT", "PATCH"])
def update_classrep():
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
@classrep_route.route("/", methods=["DELETE"])
def delete_classrep():
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
