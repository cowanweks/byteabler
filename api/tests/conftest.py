import pytest
from app import create_app
from app.extensions import db
from app.flask_config import TestingConfig


@pytest.fixture()
def app():
    app = create_app()
    app.config.from_object(TestingConfig)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
