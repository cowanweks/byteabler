from flask import (
    Blueprint,
    request,
    jsonify,
    session,
    render_template
)
from app.forms.user import UserLoginForm
from app.utils.login_utils import hash_password, verify_password
from app.models import db, User
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


index_route = Blueprint("index_route", __name__, url_prefix="/api/v1")


@index_route.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@index_route.route("/signin", methods=["POST"])
def sign_in():
    """The route that handles user signin"""

    user_form = UserLoginForm(request.form)

    try:
        if user_form.validate():
            user = db.session.query(User).filter_by(username=user_form.username.data).scalar()

            if user:
                if verify_password(user_form.password.data, user.password):
                    # Store session
                    session["username"] = user_form.username.data
                    role = db.session.query(User.roles).filter_by(username=user.username).scalar()

                    return jsonify(msg="Successfully SignedIn!", role=role), 200

            return jsonify("Incorrect username or password!"), 401

        print(user_form.errors)

        return jsonify(user_form.errors), 400

    except SQLAlchemyError as ex:
        print(ex)
        return jsonify("Database error occurred!"), 500


@index_route.route("/signout", methods=["GET"])
def sign_out():
    """The route that handles user signout"""

    return "Logout"
