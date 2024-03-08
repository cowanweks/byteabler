"""

"""
import sqlalchemy
from flask import Blueprint, request, jsonify, session
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from ..models import db, ClassReps


# Role blueprint
classrep_route = Blueprint('classrep_route', __name__,
                           url_prefix='/api/classreps')


# The route that handles classrep registration
@classrep_route.route("/new", methods=["POST"])
@jwt_required()
def new_classrep():

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    # TODO Form Validation
    data = request.get_json()

    reg_no = data.get("reg_no")
    class_id = data.get("class_id")
    firstname = data.get("firstname")
    middlename = data.get("middlename")
    lastname = data.get("lastname")
    email = data.get("email")
    phoneno = data.get("phoneno")

    db.session.add(ClassReps(reg_no=reg_no, class_id=class_id, firstname=firstname,
                             middlename=middlename, lastname=lastname, email=email, phoneno=phoneno))
    db.session.commit()

    return jsonify("Successfully Created new Role!"), 201


# The route that handles fetching a specific classrep
@classrep_route.route("/<reg_no>", methods=["GET"])
@jwt_required()
def get_classrep(reg_no):

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    results = db.session.execute(
        db.select(ClassReps).where(ClassReps.reg_no == reg_no)
    )

    classrep = results.scalars().first()

    return jsonify(classrep), 200

# A route that handles fetching multiple classrep


@classrep_route.route("/", methods=["GET"])
@jwt_required()
def get_classreps():

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    classreps = db.session.execute(
        db.select(ClassReps).order_by(ClassReps.reg_no)).scalars().all()

    return classreps, 200


# The Route that handles classrep information update
@classrep_route.route("/edit/<reg_no>", methods=["PUT", "PATCH"])
@jwt_required()
def update_classrep(reg_no):

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    data = request.get_json()

    # Validate the information entered
    if data.get('classrep_name') == None:
        return "[x] - Error, classrep is required!", 201

    classrep_name = data.get("classrep_name")

    classrep = db.session.execute(
        db.update(ClassReps).where(ClassReps.reg_no == reg_no)
        .values(classrep_name=classrep_name)
    )

    db.session.commit()

    return jsonify(msg="Successfully Updated Role!"), 200


# The route that handles classrep deletion
@classrep_route.route("/delete/<reg_no>", methods=["DELETE"])
@jwt_required()
def delete_classrep(reg_no):

    # Get the users identity
    current_user = get_jwt_identity()
    user_id_from_session = session.get('username')

    if current_user != user_id_from_session:
        return jsonify("Not authorized"), 404

    try:

        # Check for user existence then delete
        results = db.session.execute(
            db.select(ClassReps).where(ClassReps.reg_no == reg_no)
        )

        unit = results.scalars().first()

        if not unit:
            return jsonify(msg="User not found!"), 404

        # If unit exists, delete
        db.session.execute(
            db.delete(ClassReps).where(ClassReps.reg_no == reg_no)
        )
        db.session.commit()

        return jsonify(msg="Successfully Deleted Role!"), 200

    except sqlalchemy.exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(e)), 500
