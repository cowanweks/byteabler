import os
from app import create_app
from app.extensions import db
from flask_jwt_extended import JWTManager
from app.flask_config import ProductionConfig, DevelopmentConfig, TestingConfig


def main():

    # Create the flask application
    flask_app = create_app()
    JWTManager(flask_app)

    # Set the application configuration
    if os.getenv("ENV") == "production":
        flask_app.config.from_object(ProductionConfig)
    else:
        flask_app.config.from_object(DevelopmentConfig)

    # flask_app.config.from_object(TestingConfig)

    db.init_app(flask_app)

    with flask_app.app_context():
        db.create_all()

    flask_app.run(host="0.0.0.0", port=3000)


# Application Entry
if __name__ == '__main__':
    main()
