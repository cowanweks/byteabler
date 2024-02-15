import os
from app import create_app
from app.extensions import db
from app.flask_config import ProductionConfig, DevelopmentConfig


def main():

    # Create the flask application
    flask_app = create_app()

    # Set the application configuration
    if os.getenv("ENV") == "production":
        flask_app.config.from_object(ProductionConfig)
    else:
        flask_app.config.from_object(DevelopmentConfig)

    db.init_app(flask_app)

    with flask_app.app_context():
        db.create_all()

    flask_app.run(host="0.0.0.0", port=3000)


# Application Entry
if __name__ == '__main__':
    main()
