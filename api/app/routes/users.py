import json
from flask import Blueprint, request, jsonify
from bcrypt import hashpw, gensalt, checkpw
from ..models import db, Users


# A helper function that verifies user password against the hash
def hash_password(password: str) -> any:
    salt = gensalt()
    pwd = password.encode()

    # Hash the password
    hashed_pwd = hashpw(pwd, salt)
    return hashed_pwd


# User blueprint
user_route = Blueprint('user_route', __name__, static_folder='../../static',
                       template_folder='../../templates', url_prefix='/api/users')


# A route that handles fetching multiple user
@user_route.route("/", methods=["GET"])
def get_users():
    users = db.session.execute(
        db.select(Users).order_by(Users.username)).scalars().all()

    return jsonify(users), 200


# The route that handles fetching a specific user
# TODO Complete this
@user_route.route("/<username>", methods=["GET"])
def get_user(username):
    username = request.form["username"]
    return f"Hello {username}"


# The route that handles user registration
@user_route.route("/register", methods=["POST"])
def new_user():
    staff_no = request.form["staff_no"]
    username = request.form["username"]
    password = request.form["password"]
    role_name = request.form["role"]
    confirm_password = request.form["confirm_password"]

    if password != confirm_password:
        return "[x] - Passwords do not match!", 201

    db.session.add(
        Users(staff_no=staff_no, username=username, role=role_name, password=hash_password(password)))
    db.session.commit()

    return "Successfully Created new User!", 200


# The Route that handles user information update
# TODO Complete this
@user_route.route("/edit/<username>", methods=["PUT", "PATCH"])
def update_user(username):
    return "Successfully Updated User!"


# The route that handles user deletion
# TODO Complete this
@user_route.route("/delete/<username>", methods=["DELETE"])
def delete_user(username):
    return "Successfully Deleted User!"


# The route that handles user signin
@user_route.route("signin", methods=["POST"])
def signin_user():
    username = request.form["username"]
    password = request.form["password"]

    user = db.session.execute((db.select(User)).filter_by(
        username=username)).scalar_one()

    print(user)

    try:
        hashed_pwd = verify_hash(password, confirm_password)
        checkpw(password, hashed_pwd)
    except:
        return "Couldn't Signin!", 201

    return "Successfully SignedIn!", 200
