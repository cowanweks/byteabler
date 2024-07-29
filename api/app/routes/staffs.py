from app.forms.staff import StaffRegistrationForm, StaffUpdateForm
from app.models import db, Staff
from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

# Staff blueprint
staff_route = Blueprint("staff_route", __name__, url_prefix="/api/v1/staffs")


@staff_route.route("/", methods=["POST"])
def new():
    """New Staff"""

    try:
        new_staff_form = StaffRegistrationForm(request.form)

        if new_staff_form.validate():

            new_staff = Staff(
                staff_no=new_staff_form.staffNo.data,
                first_name=new_staff_form.firstName.data,
                middle_name=new_staff_form.middleName.data,
                last_name=new_staff_form.lastName.data,
                nat_id=new_staff_form.natId.data,
                phone_no=new_staff_form.mobileNo.data,
                email=new_staff_form.email.data
            )

            db.session.add(new_staff)
            db.session.commit()
            return jsonify("Successfully Created new Staff!"), 201

        else:
            print(new_staff_form.errors)
            return jsonify(new_staff_form.errors), 400

    except IntegrityError as ex:
        print(ex)
        return jsonify("Staff already exists!"), 409


@staff_route.get("/<string:unitCode>")
def get(staffNo: str):
    """Get Units"""

    try:
        staffs = db.session.query(Staff).filter_by(staff_no=staffNo).all()

        if not staffs:
            return []

        serialized_staffs = [unit.serialize() for unit in staffs]

        return jsonify(serialized_staffs), 200

    except Exception as ex:
        print(ex)
        return jsonify(f"Database error occurred! {ex}"), 500


@staff_route.get("/")
def get_staffs():
    """Get Units"""

    try:
        staffs = db.session.query(Staff).all()
        serialized_staffs = [staff.serialize() for staff in staffs]
        return jsonify(serialized_staffs), 200

    except Exception as ex:
        print(ex)
        return jsonify(f"Database error occurred! {ex}"), 500


@staff_route.route("/<string:staffNo>", methods=["PUT", "PATCH"])
def update(staffNo: str):
    """Update Unit"""

    try:
        updated_staff_form = StaffUpdateForm(request.form)

        if updated_staff_form.validate():
            db.session.execute(
                db.update(Staff)
                .where(Staff.staff_no == staffNo)
                .values(first_name=updated_staff_form.firstName.data)
            )
            db.session.commit()
            return jsonify("Successfully Updated Unit!"), 200

        else:
            return jsonify(updated_staff_form.errors), 400

    except SQLAlchemyError as ex:
        print(ex)
        return False, "Database error occurred!"


@staff_route.route("/<string:staffNo>", methods=["DELETE"])
def delete(staffNo: str):
    """Delete Unit"""

    try:
        db.session.execute(db.delete(Staff).where(Staff.staff_no == staffNo))
        db.session.commit()
        db.session.close()
        return jsonify("Successfully Deleted Unit!"), 200

    except SQLAlchemyError as ex:
        print(ex)
        db.session.close()
        return jsonify("Database error occurred!"), 500


