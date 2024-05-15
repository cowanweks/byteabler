""" """

from uuid import uuid4
from flask import Blueprint, request, jsonify
from app.models import db, Units
from sqlalchemy.exc import SQLAlchemyError


# Units blueprint
unit_route = Blueprint("unit_route", __name__, url_prefix="/bytabler/api/v1/units")


# A route that handles fetching multiple unit
@unit_route.route("/", methods=["GET"])
def get_units():
    """"""

    unit_id = request.args.get("unit_id")

    try:
        if unit_id:
            units = (
                db.session.execute(
                    db.select(Units)
                    .where(Units.unit_id == unit_id)
                    .order_by(Units.unit_id)
                )
                .scalars()
                .all()
            )

        units = (
            db.session.execute(db.select(Units).order_by(Units.unit_id)).scalars().all()
        )

        serialized_units = [unit.serialize() for unit in units]
        return jsonify(serialized_units), 200

    except SQLAlchemyError as ex:
        print(ex)
        return jsonify(msg="Database error occurred!"), 500


@unit_route.route("/", methods=["POST"])
def new_unit():
    """"""
    # TODO Form Validation
    data = request.get_json()

    unit_id = str(uuid4())
    unit_code = data.get("unit_code")
    unit_name = data.get("unit_name")

    try:
        db.session.add(Units(unit_id=unit_id, unit_code=unit_code, unit_name=unit_name))
        db.session.commit()
        return jsonify(msg="Successfully Created new Unit!"), 201

    except SQLAlchemyError as ex:
        print(str(ex))
        db.session.rollback()
        return jsonify(msg="Database error occurred!"), 500


@unit_route.route("/", methods=["PUT", "PATCH"])
def update_unit():
    """"""
    unit_id = request.args.get("unit_id")
    data = request.get_json()

    try:
        db.session.execute(
            db.update(Units).where(Units.unit_id == unit_id).values(data)
        )
        db.session.commit()
        return jsonify(msg="Successfully Updated Units!"), 201

    except SQLAlchemyError as ex:
        print(str(ex))
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


@unit_route.route("/", methods=["DELETE"])
def delete_unit():
    """"""
    unit_id = request.args.get("unit_id")

    try:
        db.session.execute(db.delete(Units).where(Units.unit_id == unit_id))
        db.session.commit()
        return jsonify(msg="Successfully Deleted Units!"), 200

    except SQLAlchemyError as ex:
        print(str(ex))
        db.session.rollback()
        return jsonify(msg="Database error occurred!"), 500
