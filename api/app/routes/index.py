from flask import (
    Blueprint,
    request,
    jsonify,
    render_template,
)
from app.controllers.login import login, logout

index_route = Blueprint("index_route", __name__, url_prefix="/api/v1")


@index_route.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@index_route.route("/signin", methods=["POST", "GET"])
def signin_user():
    """The route that handles user signin"""

    valid, response = login(request.form)

    if valid:
        return jsonify(msg=response), 200

    return jsonify(msg=response), 401


@index_route.route("/signout", methods=["GET"])
def signout_user():
    """The route that handles user signout"""

    valid, response = logout(request.args.get('user_id'))

    if valid:
        return jsonify(msg=response), 200

    return jsonify(msg=response), 500
