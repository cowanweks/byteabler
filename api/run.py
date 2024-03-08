""" Run
"""
import os
from flask_app import create_app
from app.extensions import db, sess, jwt
from app.flask_config import ProductionConfig, DevelopmentConfig


# TODO  doc strings
def main():

    # Create the flask application
    flask_app = create_app()

    # Set the application configuration
    if os.getenv("ENV") == "production":
        flask_app.config.from_object(ProductionConfig)
    else:
        flask_app.config.from_object(DevelopmentConfig)

    db.init_app(flask_app)
    jwt.init_app(flask_app)
    sess.init_app(flask_app)

    with flask_app.app_context():
        db.create_all()

    flask_app.run(host=flask_app.config.get('HOST'),
                  port=flask_app.config.get("PORT"))


# Application Entry
if __name__ == '__main__':
    main()
