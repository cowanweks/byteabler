"""

"""
import sqlalchemy
from flask import Blueprint, request, jsonify
from ..models import db, Classes


# Class blueprint
class_route = Blueprint('class_route', __name__, url_prefix='/api/classes')


# The route that handles class registration
@class_route.route("/new", methods=["POST"])
def new_class():

    # TODO Form Validation
    data = request.get_json()

    class_id = data.get("class_id")
    class_rep = data.get("class_rep")

    try:

        db.session.add(Classes(class_id=class_id, class_rep=class_rep))
        db.session.commit()

        return jsonify(msg="Successfully Created new Class!"), 201

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


# The route that handles fetching a specific class
@class_route.route("/<class_id>", methods=["GET"])
def get_class(class_id):

    try:

        results = db.session.execute(
            db.select(Classes).where(Classes.class_id == class_id))

        class_ = results.scalars().first()

        if not class_:
            return jsonify(msg="Class not found"), 404

        return jsonify(class_), 200

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


# A route that handles fetching multiple class
@class_route.route("/", methods=["GET"])
def get_classes():

    try:

        classes = db.session.execute(
            db.select(Classes).order_by(Classes.class_id)).scalars().all()

        return classes, 200

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


# The Route that handles class information update
@class_route.route("/edit/<class_id>", methods=["PUT", "PATCH"])
def update_class(class_id):

    data = request.get_json()

    class_rep = data.get("class_rep")

    # Validate the information entered
    if class_rep == None:
        return jsonify(msg="Error, class is required!"), 400

    try:

        results = db.session.execute(
            db.select(Classes).where(Classes.class_id == class_id))

        class_ = results.scalars().first()

        if class_ == None:
            return jsonify(msg="Error, class not found!"), 404

        db.session.execute(
            db.update(Classes).where(Classes.class_id == class_id)
            .values(class_rep=class_rep)
        )
        db.session.commit()

        return jsonify(msg="Successfully Updated Class!"), 201

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


# The route that handles class deletion
@class_route.route("/delete/<class_id>", methods=["DELETE"])
def delete_class(class_id):

    try:

        # Check for user existence then delete
        results = db.session.execute(
            db.select(Classes).where(Classes.class_id == class_id)
        )

        class_ = results.scalars().first()

        if not class_:
            return jsonify(msg="Class not found!"), 404

        # If unit exists, delete
        db.session.execute(
            db.delete(Classes).where(Classes.class_id == class_id)
        )
        db.session.commit()

        return jsonify(msg="Successfully Deleted Class!"), 200

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500
