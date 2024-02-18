from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from .error_handlers import not_found
from .routes import user_route, role_route
from .models import Users


# Load environment variables
load_dotenv(find_dotenv())


def create_app():
    app = Flask(__name__, static_folder='../static',
                template_folder='../templates')

    # Prevent redirects in blueprints
    app.url_map.strict_slashes = False

    # Register blueprints
    app.register_blueprint(user_route)
    app.register_blueprint(role_route)

    # Register error handlers
    app.register_error_handler(404, not_found)

    @app.route("/", methods=["GET"])
    @app.route("/api", methods=["GET"])
    def index():
        return render_template("index.html")

    JWTManager(app)

    return app
