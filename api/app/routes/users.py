from flask import Blueprint, request, jsonify
from app.models import db, Users
from app.utils.login_utils import hash_password
from uuid import uuid4
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


# User blueprint
user_route = Blueprint("user_route", __name__, url_prefix="/bytabler/api/v1/users")


@user_route.route("/", methods=["POST"])
def new_user():
    """The route that handles user registration"""

    data = request.get_json()

    user_id = str(uuid4())
    staff_no = data.get("staff_no")
    username = data.get("username")
    role_name = data.get("role_id")
    password = data.get("password")
    confirm_password = data.get("confirm_password")

    try:
        if password != confirm_password:
            return jsonify("[x] - Passwords do not match!"), 400

        db.session.execute(
            db.insert(Users).values(
                user_id=user_id,
                staff_no=staff_no,
                username=username,
                role=role_name,
                password=hash_password(password),
            )
        )
        db.session.commit()
        return jsonify(msg="Successfully Created new User!"), 201

    except IntegrityError as ex:
        print(ex)
        return jsonify(msg="[x] - User already exists!"), 400


# A route that handles fetching multiple user
@user_route.route("/", methods=["GET"])
def get_users():
    """Get the users"""

    user_id = request.args.get("user_id")

    try:
        if user_id:
            users = (
                db.session.execute(
                    db.select(Users)
                    .where(Users.user_id == user_id)
                    .order_by(Users.user_id)
                )
                .scalars()
                .all()
            )
        users = (
            db.session.execute(db.select(Users).order_by(Users.user_id)).scalars().all()
        )

        serialized_users = [user.serialize() for user in users]
        return jsonify(serialized_users), 200

    except SQLAlchemyError as ex:
        return jsonify(msg="Database error occurred!", error=str(ex)), 500


# The Route that handles user information update
# TODO Complete this
@user_route.route("/", methods=["PUT", "PATCH"])
def update_user():
    """Update User"""

    user_id = request.args.get("user_id")

    data = request.get_json()
    role_id = data.get("role_id")
    password = data.get("password")
    confirm_password = data.get("confirm_password")

    if password != confirm_password:
        return jsonify(error="Password don't match"), 400

    try:
        db.session.execute(
            db.update(Users)
            .where(Users.user_id == user_id)
            .values(password=hash_password(password), role=role_id)
        )
        db.session.commit()
        return jsonify(msg="Successfully Updated User!"), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


# The route that handles user deletion
# TODO Complete this
@user_route.route("/", methods=["DELETE"])
def delete_user():
    """Delete User"""

    user_id = request.args.get("user_id")

    try:
        db.session.execute(db.delete(Users).where(Users.user_id == user_id))
        db.session.commit()
        db.session.close()
        return jsonify(msg="Successfully Deleted User!"), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        db.session.close()
        return jsonify(msg="Database error occurred!", error=str(e)), 500
