from .models import flask_app

# Import Blueprints
from .routes import user_route, role_route

# Import Models
from .models import Users


# Register blueprints
flask_app.register_blueprint(user_route)
flask_app.register_blueprint(role_route)
