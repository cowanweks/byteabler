from flask import Blueprint, request, jsonify
from uuid import uuid4
from app.models import db, User
from app.forms.user import UserRegistrationForm, UserUpdateForm, UserLoginForm, UserUpdatePasswordForm
from app.utils.login_utils import hash_password, verify_password
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

# User blueprint
user_route = Blueprint("user_route", __name__, url_prefix="/api/v1/users")


@user_route.route("/", methods=["POST"])
def new():
    """New User"""

    try:
        new_user_form = UserRegistrationForm(request.form)

        if new_user_form.validate():
            new_user = User(
                user_id=str(uuid4()),
                staff_no=new_user_form.staff_no.data,
                username=new_user_form.username.data,
                roles=new_user_form.roles.data,
                password=hash_password(new_user_form.password.data))

            db.session.add(new_user)
            db.session.commit()
            return jsonify("Successfully Created new User!"), 200

        else:
            return jsonify(new_user_form.errors), 400

    except IntegrityError as ex:
        print(ex)
        return jsonify("User already exists!"), 400


@user_route.route("/<string:user_id>", methods=["GET"])
def get(user_id: str):
    """Get the users"""

    try:
        users = (
            db.session.query(User).order_by(User.user_id).all()
        )

        serialized_users = [user.serialize() for user in users]
        return jsonify(serialized_users), 200

    except Exception as ex:
        print(ex)
        return jsonify("Database error occurred!"), 500


@user_route.route("/", methods=["GET"])
def get_users():
    """Get the users"""

    try:
        users = db.session.query(User).order_by(User.user_id).all()

        serialized_users = [user.serialize() for user in users]
        return jsonify(serialized_users), 200

    except Exception as ex:
        print(ex)
        return jsonify("Database error occurred!"), 500


@user_route.route("/<string:user_id>", methods=["PUT", "PATCH"])
def update(user_id: str):
    """Update User"""

    try:
        updated_user_form = UserUpdateForm(request.form)

        if updated_user_form.validate():
            db.session.execute(
                db.update(User)
                .where(User.user_id == user_id)
                .values(roles=updated_user_form.roles.data)
            )
            db.session.commit()
            return jsonify("Successfully Updated User!"), 200

        else:
            return jsonify(updated_user_form.errors), 500

    except SQLAlchemyError as ex:
        print(ex)
        return jsonify("Database error occurred!"), 500


@user_route.route("/<string:user_id>", methods=["DELETE"])
def delete(user_id: str):
    """Delete User"""

    try:
        db.session.execute(db.delete(User).where(User.user_id == user_id))
        db.session.commit()
        db.session.close()
        return jsonify("Successfully Deleted User!"), 200

    except SQLAlchemyError as ex:
        print(ex)
        db.session.close()
        return jsonify("Database error occurred!"), 500
