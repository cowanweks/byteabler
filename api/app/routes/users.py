import json
import sqlalchemy
from flask import Blueprint, request, jsonify, session
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from bcrypt import hashpw, gensalt, checkpw
from ..models import db, Users


# User blueprint
user_route = Blueprint('user_route', __name__, url_prefix='/api/users')


# A helper function that verifies user password against the hash
def hash_password(password: str) -> str:
    salt = gensalt()
    pwd = password.encode()

    # Hash the password
    hashed_pwd = hashpw(pwd, salt)
    return hashed_pwd


# The route that handles user signin
@user_route.route("/signin", methods=["POST"])
def signin_user():

    data = request.get_json()

    username: str = data.get("username")
    password: str = data.get("password")

    results = db.session.execute(
        db.select(Users).where(Users.username == username)
    )

    user = results.scalars().first()

    if not user:
        return jsonify({"msg": "User not found!"}), 404

    if checkpw(password.encode(), user.password):
        access_token = create_access_token(identity=username)

        # Store session
        session['username'] = username

        return jsonify(msg="Successfully SignedIn!", access_token=f"Bearer {access_token}"), 200

    return jsonify(msg="[x] - Incorrect username or password!"), 401


# The route that handles user registration

@user_route.route("/new", methods=["POST"])
def new_user():

    data = request.get_json()

    staff_no = data.get("staff_no")
    username = data.get("username")
    email = data.get("email")
    role_name = data.get("role_id")
    password = data.get("password")
    confirm_password = data.get("confirm_password")

    try:

        if password != confirm_password:
            return jsonify("[x] - Passwords do not match!"), 400

        db.session.execute(
            db.insert(Users).values(staff_no=staff_no, username=username,
                                    role=role_name, password=hash_password(password))
        )

        db.session.commit()

        return jsonify(msg="Successfully Created new User!"), 201

    except:
        return jsonify(msg="Couldn't Create new User!"), 400


# The route that handles fetching a specific user
# TODO Complete this
@user_route.route("/<username>", methods=["GET"])
@jwt_required()
def get_user(username):

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    try:
        results = db.session.execute(
            db.select(Users).where(Users.username == username)
        )
        user = results.scalars().first()

        if user:
            return jsonify(user), 200

        return jsonify(msg="User not found"), 404

    except sqlalchemy.exc.SQLAlchemyError as e:
        return jsonify(msg="Database error occurred!", error=str(e)), 500


# A route that handles fetching multiple user
@user_route.route("/", methods=["GET"])
@jwt_required()
def get_users():

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    try:

        users = db.session.execute(
            db.select(Users).order_by(Users.staff_no)).scalars().all()

        if users:
            return jsonify(users), 200

        return jsonify(msg="No Users Found!"), 404

    except sqlalchemy.exc.SQLAlchemyError as e:
        return jsonify(msg="Database error occurred!", error=str(e)), 500


# The Route that handles user information update
# TODO Complete this
@user_route.route("/edit/<username>", methods=["PUT", "PATCH"])
@jwt_required()
def update_user(username):

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    data = request.get_json()

    email = data.get("email")
    role_id = data.get("role_id")
    username = data.get("username")
    password = data.get("password")
    confirm_password = data.get("confirm_password")

    if password != confirm_password:
        return jsonify(error="Password don't match"), 400

    try:
        db.session.execute(
            db.update(Users).where(Users.username == username).values(
                password=hash_password(password), role=role_id)
        )
        db.session.commit()
        return jsonify(msg="Successfully Updated User!"), 201

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500


# The route that handles user deletion
# TODO Complete this
@user_route.route("/delete/<username>", methods=["DELETE"])
@jwt_required()
def delete_user(username):

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    try:

        # Check for user existence then delete
        results = db.session.execute(
            db.select(Users).where(Users.username == username)
        )

        user = results.scalars().first()

        if not user:
            return jsonify(msg="User not found!"), 404

        # If user exists, delete
        db.session.execute(
            db.delete(Users).where(Users.username == username)
        )

        db.session.commit()

        return jsonify(msg="Successfully Deleted User!"), 200

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500
