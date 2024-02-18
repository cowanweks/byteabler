"""

"""
from flask import Blueprint, request, jsonify
from bcrypt import hashpw, gensalt, checkpw
from ..models import db, Roles


# Role blueprint
role_route = Blueprint('role_route', __name__, static_folder='../../static',
                       template_folder='../../templates', url_prefix='/api/roles')


# A route that handles fetching multiple role
@role_route.route("/", methods=["GET"])
def get_roles():
    roles = []
    roles = db.session.execute(
        db.select(Roles).order_by(Roles.rolename)).scalars().all()

    return roles, 200


# The route that handles fetching a specific role
@role_route.route("/<rolename>", methods=["GET"])
def get_role(rolename):
    rolename = request.form["role"]
    return f"Hello {rolename}"


# The route that handles role registration
@role_route.route("/register", methods=["POST"])
def new_role():
    # TODO Form Validation
    rolename = request.form["role"]

    db.session.add(Roles(role=rolename))
    db.session.commit()

    return "Successfully Created new Role!"


# The Route that handles role information update
@role_route.route("/edit/<rolename>", methods=["PUT", "PATCH"])
def update_role(rolename):
    # Validate the information entered
    if request.form['role'] == None:
        return "[x] - Error, role is required!", 201

    role = db.session.query(Roles).filter_by(role=rolename).one()

    print(role)

    return "Successfully Updated Role!", 200


# The route that handles role deletion
@role_route.route("/delete/<rolename>", methods=["DELETE"])
def delete_role(rolename):
    return "Successfully Deleted Role!"


# The route that handles role signin
@role_route.route("signin", methods=["POST"])
def signin_role():
    rolename = request.form["rolename"]
    password = request.form["password"]

    role = db.session.execute((db.select(Role)).filter_by(
        rolename=rolename)).scalar_one()

    print(role)

    try:
        hashed_pwd = verify_hash(password, confirm_password)
        checkpw(password, hashed_pwd)
    except:
        return "Couldn't Signin!", 201

    return "Successfully SignedIn!", 200
