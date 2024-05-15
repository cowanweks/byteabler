from flask import (
    Blueprint,
    request,
    jsonify,
    session,
    render_template,
)
from sqlalchemy.exc import SQLAlchemyError
from app.utils.login_utils import verify_password
from app.models import db, Users


index_route = Blueprint("index_route", __name__, url_prefix="/bytabler/api/v1")


@index_route.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@index_route.route("/signin", methods=["POST", "GET"])
def signin_user():
    """The route that handles user signin"""

    data = request.get_json()

    username: str = data.get("username")
    password: str = data.get("password")

    try:
        results = db.session.execute(db.select(Users).where(Users.username == username))
        user = results.scalars().first()

        if user:
            if verify_password(password, user.password):
                # Store session
                session["username"] = username

                return jsonify(msg="Successfully SignedIn!"), 200

        return jsonify(msg="[x] - Incorrect username or password!"), 401

    except SQLAlchemyError as ex:
        db.session.rollback()
        return jsonify(msg="Database error occurred!", error=str(ex)), 500


@index_route.route("/signout", methods=["GET"])
def signout_user():
    """The route that handles user signout"""

    print(request)

    return {"msg": "[x] - Authentication failed!"}, 200
