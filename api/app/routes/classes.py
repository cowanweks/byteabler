""" """

from uuid import uuid4
import sqlalchemy
from flask import Blueprint, request, jsonify
from app.models import db, Classes


# Class blueprint
class_route = Blueprint("class_route", __name__, url_prefix="/bytabler/api/v1/classes")


# The route that handles class registration
@class_route.route("/", methods=["POST"])
def new_class():
    # TODO Form Validation
    data = request.get_json()
    class_id = str(uuid4())
    class_rep = data.get("class_rep")

    try:
        db.session.add(Classes(class_id=class_id, class_rep=class_rep))
        db.session.commit()
        return jsonify(msg="Successfully Created new Class!"), 201

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


# A route that handles fetching multiple class
@class_route.route("/", methods=["GET"])
def get_classes():
    """"""
    class_id = request.args.get("class_id")

    try:
        if class_id:
            classes = (
                db.session.execute(
                    db.select(Classes)
                    .where(Classes.class_id == class_id)
                    .order_by(Classes.class_id)
                )
                .scalars()
                .all()
            )

        classes = (
            db.session.execute(db.select(Classes).order_by(Classes.class_id))
            .scalars()
            .all()
        )

        serialized_classes = [classs.serialize() for classs in classes]
        return jsonify(serialized_classes), 200

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


# The Route that handles class information update
@class_route.route("/", methods=["PUT", "PATCH"])
def update_class():
    """"""
    class_id = request.args.get("class_id")
    class_rep = request.form.get("class_rep")

    try:
        db.session.execute(
            db.update(Classes)
            .where(Classes.class_id == class_id)
            .values(class_rep=class_rep)
        )
        db.session.commit()
        return jsonify(msg="Successfully Updated Class!"), 201

    except sqlalchemy.exc.SQLAlchemyError as ex:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(ex)), 500


# The route that handles class deletion
@class_route.route("/", methods=["DELETE"])
def delete_class():
    """"""
    class_id = request.args.get("class_id")

    try:
        db.session.execute(db.delete(Classes).where(Classes.class_id == class_id))
        db.session.commit()
        return jsonify(msg="Successfully Deleted Class!"), 200

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500
