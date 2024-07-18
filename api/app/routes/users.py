from flask import Blueprint, request, jsonify
from uuid import uuid4
from app.models import db, User
from app.forms.user import UserRegistrationForm, UserUpdateForm, UserLoginForm, UserUpdatePasswordForm
from app.utils.login_utils import hash_password, verify_password
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

# User blueprint
user_route = Blueprint("user_route", __name__, url_prefix="/api/v1/users")


@user_route.route("/", methods=["POST"])
def new_user_route():
    """New User"""

    try:
        new_user_form = UserRegistrationForm(request.form)

        if new_user_form.validate():
            db.session.execute(
                db.insert(User).values(
                    user_id=str(uuid4()),
                    staff_no=new_user_form.staff_no.data,
                    username=new_user_form.username.data,
                    roles=new_user_form.roles.data,
                    password=hash_password(new_user_form.password.data)
                )
            )
            db.session.commit()
            return True, "Successfully Created new User!"

        else:
            print(new_user_form.errors)
            return False, new_user_form.errors

    except IntegrityError as ex:
        print(ex)
        return False, "User already exists!"


@user_route.route("/<string:user_id>", methods=["GET"])
def get_user_route(user_id: str):
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
def get_users_route():
    """Get the users"""

    try:
        users = db.session.query(User).order_by(User.user_id).all()

        serialized_users = [user.serialize() for user in users]
        return jsonify(serialized_users), 200

    except Exception as ex:
        print(ex)
        return jsonify("Database error occurred!"), 500


@user_route.route("/<string:user_id>", methods=["PUT", "PATCH"])
def update_user_route(user_id: str):
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
            return True, "Successfully Updated User!"

        else:
            return False, updated_user_form.errors

    except SQLAlchemyError as ex:
        print(ex)
        return False, "Database error occurred!"


@user_route.route("/<string:user_id>", methods=["DELETE"])
def delete_user_route(user_id: str):
    """Delete User"""

    try:
        db.session.execute(db.delete(User).where(User.user_id == user_id))
        db.session.commit()
        db.session.close()
        return True, "Successfully Deleted User!"

    except SQLAlchemyError as ex:
        print(ex)
        db.session.close()
        return False, "Database error occurred!"


def signin_user_route():
    """"""
    pass


def signout_user_route():
    pass
