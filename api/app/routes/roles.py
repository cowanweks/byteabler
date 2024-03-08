"""

"""
import sqlalchemy
from flask import Blueprint, request, jsonify, session
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from ..models import db, Roles


# Role blueprint
role_route = Blueprint('role_route', __name__, url_prefix='/api/roles')


# The route that handles role registration
@role_route.route("/new", methods=["POST"])
@jwt_required()
def new_role():

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    # TODO Form Validation
    data = request.get_json()

    role_id = data.get("role_id")
    role_name = data.get("role_name")

    db.session.add(Roles(role_id=role_id, role_name=role_name))
    db.session.commit()

    return jsonify("Successfully Created new Role!"), 201


# The route that handles fetching a specific role
@role_route.route("/<role_id>", methods=["GET"])
@jwt_required()
def get_role(role_id):

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    results = db.session.execute(
        db.select(Roles).where(Roles.role_id == role_id)
    )

    role = results.scalars().first()

    return jsonify(role), 200

# A route that handles fetching multiple role


@role_route.route("/", methods=["GET"])
@jwt_required()
def get_roles():

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    roles = db.session.execute(
        db.select(Roles).order_by(Roles.role_id)).scalars().all()

    return roles, 200


# The Route that handles role information update
@role_route.route("/edit/<role_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_role(role_id):

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    data = request.get_json()

    # Validate the information entered
    if data.get('role_name') == None:
        return "[x] - Error, role is required!", 201

    role_name = data.get("role_name")

    role = db.session.execute(
        db.update(Roles).where(Roles.role_id == role_id)
        .values(role_name=role_name)
    )

    db.session.commit()

    return jsonify(msg="Successfully Updated Role!"), 200


# The route that handles role deletion
@role_route.route("/delete/<role_id>", methods=["DELETE"])
@jwt_required()
def delete_role(role_id):

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    try:

        # Check for user existence then delete
        results = db.session.execute(
            db.select(Roles).where(Roles.role_id == role_id)
        )

        unit = results.scalars().first()

        if not unit:
            return jsonify(msg="User not found!"), 404

        # If unit exists, delete
        db.session.execute(
            db.delete(Roles).where(Roles.role_id == role_id)
        )
        db.session.commit()

        return jsonify(msg="Successfully Deleted Role!"), 200

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500
