from flask import Flask, render_template

flask_app = Flask(__name__, static_folder='../static',
                  template_folder='../templates')

# Prevent redirects in blueprints
flask_app.url_map.strict_slashes = False


@flask_app.route("/", methods=["GET"])
@flask_app.route("/api", methods=["GET"])
def index():
    return render_template("index.html")
