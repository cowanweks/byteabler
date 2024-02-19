"""

"""
import sqlalchemy
from flask import Blueprint, request, jsonify
from ..models import db, Units


# Units blueprint
unit_route = Blueprint('unit_route', __name__, static_folder='../../static',
                       template_folder='../../templates', url_prefix='/api/units')


# A route that handles fetching multiple unit
@unit_route.route("/", methods=["GET"])
def get_units():

    units = db.session.execute(
        db.select(Units).order_by(Units.unit_code)).scalars().all()

    return jsonify(units), 200


# The route that handles fetching a specific unit
@unit_route.route("/<unit_code>", methods=["GET"])
def get_unit(unit_code):

    results = db.session.execute(
        db.select(Units).where(Units.unit_code == unit_code)
    )

    unit = results.scalars().first()

    return jsonify(unit), 200


# The route that handles unit registration
@unit_route.route("/new", methods=["POST"])
def new_unit():

    # TODO Form Validation
    data = request.get_json()

    unit_code = data.get("unit_code")
    unit_name = data.get("unit_name")

    try:
        db.session.add(Units(unit_code=unit_code, unit_name=unit_name))
        db.session.commit()
        return jsonify(msg="Successfully Created new Unit!"), 201

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


# The Route that handles unit information update
@unit_route.route("/edit/<unit_code>", methods=["PUT", "PATCH"])
def update_unit(unit_code):

    data = request.get_json()

    # Validate the information entered
    if data.get('unit_name') == None:
        return jsonify(msg="Error, unit is required!"), 400

    unit_name = data.get("unit_name")

    try:
        unit = db.session.execute(
            db.update(Units).where(Units.unit_code == unit_code)
            .values(unit_name=unit_name)
        )
        db.session.commit()

        return jsonify(msg="Successfully Updated Units!"), 201

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


# The route that handles unit deletion
@unit_route.route("/delete/<unit_code>", methods=["DELETE"])
def delete_unit(unit_code):
    try:

        # Check for user existence then delete
        results = db.session.execute(
            db.select(Units).where(Units.unit_code == unit_code)
        )

        unit = results.scalars().first()

        if not unit:
            return jsonify(msg="User not found!"), 404

        # If unit exists, delete
        db.session.execute(
            db.delete(Units).where(Units.unit_code == unit_code)
        )
        db.session.commit()

        return jsonify(msg="Successfully Deleted Units!"), 200

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500
