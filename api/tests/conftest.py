import pytest
from app import create_app
from app.config.flask_config import TestingConfig


@pytest.fixture()
def app():
    """Create the flask application to be tested!"""
    flask_app = create_app()
    flask_app.config.from_object(TestingConfig)

    yield flask_app


@pytest.fixture()
def client(app):
    """The applications test client"""
    yield app.test_client()


@pytest.fixture()
def runner(app):
    yield app.test_cli_runner()
