from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from bcrypt import hashpw, gensalt, checkpw
from ..models import db, Users


# User blueprint
user_route = Blueprint('user_route', __name__, static_folder='../../static',
                       template_folder='../../templates', url_prefix='/api/users')


# A helper function that verifies user password against the hash
def hash_password(password: str) -> str:
    salt = gensalt()
    pwd = password.encode()

    # Hash the password
    hashed_pwd = hashpw(pwd, salt)
    return hashed_pwd


# A route that handles fetching multiple user
@user_route.route("/", methods=["GET"])
@jwt_required()
def get_users():
    users = db.session.execute(
        db.select(Users).order_by(Users.staff_no)).scalars().all()

    return jsonify(users), 200


# The route that handles fetching a specific user
# TODO Complete this
@user_route.route("/<username>", methods=["GET"])
@jwt_required()
def get_user(username):
    username = request.form["username"]

    # Get the users identity
    current_user = get_jwt_identity()

    user = db.session.execute((db.select(User)).filter_by(
        username=username)).scalar_one()

    return jsonify(user=user), 200


# The route that handles user registration
@user_route.route("/register", methods=["POST"])
@jwt_required()
def new_user():
    staff_no = request.form["staff_no"]
    username = request.form["username"]
    password = request.form["password"]
    role_name = request.form["role"]
    confirm_password = request.form["confirm_password"]

    # Get the users identity
    current_user = get_jwt_identity()

    if password != confirm_password:
        return jsonify("[x] - Passwords do not match!"), 201

    db.session.add(
        Users(staff_no=staff_no, username=username, role=role_name, password=hash_password(password)))
    db.session.commit()

    return jsonify(msg="Successfully Created new User!"), 200


# The Route that handles user information update
# TODO Complete this
@user_route.route("/edit/<username>", methods=["PUT", "PATCH"])
@jwt_required()
def update_user(username):
    # Get the users identity
    current_user = get_jwt_identity()
    return "Successfully Updated User!"


# The route that handles user deletion
# TODO Complete this
@user_route.route("/delete/<username>", methods=["DELETE"])
@jwt_required()
def delete_user(username):
    # Get the users identity
    current_user = get_jwt_identity()
    return jsonify("Successfully Deleted User!"), 200


# The route that handles user signin
@user_route.route("signin", methods=["POST"])
def signin_user():
    username = request.form["username"]
    password = request.form["password"]

    user = db.session.execute((db.select(User)).filter_by(
        username=username)).scalar_one()

    try:
        hashed_pwd = hash_password(password)
        checkpw(password, hashed_pwd)
    except:
        return jsonify(msg="[x] - Incorrect username or password!"), 201

    access_token = create_access_token(identity=username)

    return jsonify(msg="Successfully SignedIn!", access_token=access_token), 200
