""" """

from uuid import uuid4
import sqlalchemy
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from app.models import db, Role


# Role blueprint
role_route = Blueprint("role_route", __name__, url_prefix="/api/v1/roles")


# The route that handles role registration
@role_route.route("/", methods=["POST"])
def new():
    # Get the users identity

    # TODO Form Validation
    data = request.get_json()

    role_id = str(uuid4())
    role_name = data.get("role_name")
    role_description = data.get("role_description")

    print(role_description)

    try:
        db.session.add(
            Role(
                role_id=role_id, role_name=role_name, role_description=role_description
            )
        )
        db.session.commit()
        return jsonify("Successfully Created new Role!"), 201

    except IntegrityError as ex:
        print("{}".format(ex))
        db.session.rollback()
        return jsonify(msg="Role already exists!"), 400


@role_route.route("/<string:role_id>", methods=["GET"])
def get(role_id: str):
    """Get the Role"""

    try:
        roles = db.session.query(Role).filter_by(role_id == role_id).all()

        serialized_roles = [role.serialize() for role in roles]
        return jsonify(serialized_roles), 200

    except SQLAlchemyError as ex:
        print(str(ex))
        return jsonify(msg="Database error occurred!"), 500


@role_route.route("/", methods=["GET"])
def get_roles():
    """Get Roles"""

    try:
        roles = db.session.query(Role).all()

        serialized_roles = [role.serialize() for role in roles]
        return jsonify(serialized_roles), 200

    except SQLAlchemyError as ex:
        print(str(ex))
        return jsonify(msg="Database error occurred!"), 500


# The Route that handles role information update
@role_route.route("/", methods=["PUT", "PATCH"])
def update():
    """"""
    role_id = request.args.get("role_id")
    data = request.get_json()

    try:
        db.session.execute(
            db.update(Role).where(Role.role_id == role_id).values(data)
        )
        db.session.commit()
        return jsonify(msg="Successfully Updated Role!"), 200

    except SQLAlchemyError as ex:
        print(str(ex))
        db.session.rollback()
        return jsonify(msg="Database error occurred!"), 500


# The route that handles role deletion
@role_route.route("/", methods=["DELETE"])
def delete():
    """"""
    role_id = request.args.get("role_id")

    try:
        db.session.execute(db.delete(Role).where(Role.role_id == role_id))
        db.session.commit()
        return jsonify(msg="Successfully Deleted Role!"), 200

    except sqlalchemy.exc.SQLAlchemyError as ex:
        print(str(ex))
        db.session.rollback()
        return jsonify(msg="Database error occurred!"), 500
