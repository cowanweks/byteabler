""" """

from uuid import uuid4
import sqlalchemy
from flask import Blueprint, request, jsonify
from app.models import db, Class
from app.forms.classes import ClassRegistrationForm, ClassUpdateForm


# Class blueprint
class_route = Blueprint("class_route", __name__, url_prefix="/api/v1/classes")


@class_route.route("/", methods=["POST"])
def new():
    """The route that handles class registration"""
    form = ClassRegistrationForm(request.form)

    if form.validate():

        new_class = Class(class_id=form.classId.data, class_rep=form.classRep.data)

        try:
            db.session.add(new_class)
            db.session.commit()
            return jsonify(msg="Successfully Created new Class!"), 201

        except sqlalchemy.exc.IntegrityError as ex:
            return jsonify("Class Already Exists"), 409

        except sqlalchemy.exc.SQLAlchemyError as ex:
            return jsonify(msg="Database error occurred!", error=str(ex)), 500

    return jsonify(form.errors), 400


@class_route.route("/<string:class_id>", methods=["GET"])
def get(class_id: str):
    """A route that handles fetching multiple class"""

    try:
        classes = db.session.query(Class).filter_by(class_id=class_id)

        serialized_classes = [_class.serialize() for _class in classes]
        return jsonify(serialized_classes), 200

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


@class_route.route("/", methods=["GET"])
def get_classes_route():
    """A route that handles fetching multiple class"""

    try:
        classes = db.session.query(Class).all()

        serialized_classes = [_class.serialize() for _class in classes]
        return jsonify(serialized_classes), 200

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


@class_route.route("/", methods=["PUT", "PATCH"])
def update():
    """The Route that handles class information update"""
    class_id = request.args.get("class_id")
    class_rep = request.form.get("class_rep")

    try:
        db.session.execute(
            db.update(Class)
            .where(Class.class_id == class_id)
            .values(class_rep=class_rep)
        )
        db.session.commit()
        return jsonify(msg="Successfully Updated Class!"), 201

    except sqlalchemy.exc.SQLAlchemyError as ex:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(ex)), 500


# The route that handles class deletion
@class_route.route("/", methods=["DELETE"])
def delete():
    """"""
    class_id = request.args.get("class_id")

    try:
        db.session.execute(db.delete(Class).where(Class.class_id == class_id))
        db.session.commit()
        return jsonify(msg="Successfully Deleted Class!"), 200

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500
