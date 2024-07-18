from app.models import db, Unit
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.forms.unit import UnitRegistrationForm, UnitUpdateForm

# Units blueprint
unit_route = Blueprint("unit_route", __name__, url_prefix="/api/v1/units")


@unit_route.route("/", methods=["POST"])
def new_unit_route():
    """New Unit"""

    try:
        new_unit_form = UnitRegistrationForm(request.form)

        if new_unit_form.validate():
            db.session.execute(
                db.insert(Unit).values(
                    unit_code=new_unit_form.unitCode.data,
                    unit_name=new_unit_form.unitName.data
                )
            )
            db.session.commit()
            return jsonify("Successfully Created new Unit!"), 201

        else:
            print(new_unit_form.errors)
            return jsonify(new_unit_form.errors), 400

    except IntegrityError as ex:
        print(ex)
        return jsonify("Unit already exists!"), 400


@unit_route.get("/<string:unitCode>")
def get_unit_route(unitCode: str):
    """Get Units"""

    try:
        units = db.session.query(Unit).filter_by(unit_code=unitCode).all()

        if not units:
            return []

        serialized_units = [unit.serialize() for unit in units]

        return jsonify(serialized_units), 200

    except Exception as ex:
        print(ex)
        return jsonify(f"Database error occurred! {ex}"), 500


@unit_route.get("/")
def get_units_route():
    """Get Units"""

    try:
        units = db.session.query(Unit).all()
        serialized_units = [unit.serialize() for unit in units]
        return jsonify(serialized_units), 200

    except Exception as ex:
        print(ex)
        return jsonify(f"Database error occurred! {ex}"), 500


@unit_route.route("/<string:unitCode>", methods=["PUT", "PATCH"])
def update_user_route(unitCode: str):
    """Update Unit"""

    try:
        updated_unit_form = UnitUpdateForm(request.form)

        if updated_unit_form.validate():
            db.session.execute(
                db.update(Unit)
                .where(Unit.unit_code == unitCode)
                .values(unit_name=updated_unit_form.unit_name.data)
            )
            db.session.commit()
            return jsonify("Successfully Updated Unit!"), 200

        else:
            return jsonify(updated_unit_form.errors), 400

    except SQLAlchemyError as ex:
        print(ex)
        return False, "Database error occurred!"


@unit_route.route("/<string:unitCode>", methods=["DELETE"])
def delete_user_route(unitCode: str):
    """Delete Unit"""

    try:
        db.session.execute(db.delete(Unit).where(Unit.unit_code == unitCode))
        db.session.commit()
        db.session.close()
        return jsonify("Successfully Deleted Unit!"), 200

    except SQLAlchemyError as ex:
        print(ex)
        db.session.close()
        return jsonify("Database error occurred!"), 500


