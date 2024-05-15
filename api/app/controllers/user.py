from uuid import uuid4
from app.models import db, Users
from app.utils.login_utils import hash_password
from sqlalchemy.exc import IntegrityError


# TODO: Make changes to this
"""A controller that handles new user registrations"""


def new_user(data: list[dict]) -> bool:
    return True


""""""


def get_users():
    pass


""""""


def delete_user():
    pass


""""""


def update_user():
    pass
