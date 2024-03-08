from flask import Flask, render_template
from app.routes import user_route, role_route, unit_route, class_route, classrep_route
from app.error_handlers import not_found


def create_app():
    app = Flask(__name__, static_folder="static",
                template_folder="templates")

    # Prevent redirects in blueprints
    app.url_map.strict_slashes = False

    # Register blueprints
    app.register_blueprint(user_route)
    app.register_blueprint(role_route)
    app.register_blueprint(unit_route)
    app.register_blueprint(class_route)
    app.register_blueprint(classrep_route)

    # Register error handlers
    app.register_error_handler(404, not_found)

    @app.route("/", methods=["GET"])
    @app.route("/api", methods=["GET"])
    def index():
        return render_template("index.html")

    return app
